
import argparse
import csv
import datetime as dt
import hashlib
import json
import re
import time
from typing import Dict, List, Optional, Any

import requests
import yaml

SEEN_FILE = ".seen_jobs.json"
OUTPUT_FILE = "jobs_latest.csv"
USER_AGENT = "MarketingJobFinder/1.0 (+https://example.com)"
TIMEOUT = 20

def load_config(path: str) -> Dict[str, Any]:
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)

def load_seen(path: str) -> Dict[str, float]:
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def save_seen(path: str, seen: Dict[str, float]) -> None:
    with open(path, "w", encoding="utf-8") as f:
        json.dump(seen, f, indent=2, sort_keys=True)

def http_get_json(url: str, params: Optional[dict]=None, headers: Optional[dict]=None) -> Optional[dict]:
    hdrs = {"User-Agent": USER_AGENT, "Accept": "application/json"}
    if headers:
        hdrs.update(headers)
    try:
        r = requests.get(url, params=params, headers=hdrs, timeout=TIMEOUT)
        r.raise_for_status()
        # Some endpoints return list at top level
        try:
            return r.json()
        except ValueError:
            return None
    except requests.RequestException:
        return None

def normalize_text(s: Optional[str]) -> str:
    return (s or "").strip()

def matches_filters(title: str, location: str, include_keywords: List[str], location_keywords: Optional[List[str]], exclude_keywords: Optional[List[str]]) -> bool:
    t = title.lower()
    loc = location.lower()
    if include_keywords:
        if not any(k.lower() in t for k in include_keywords):
            return False
    if location_keywords:
        if not any(k.lower() in loc for k in location_keywords):
            return False
    if exclude_keywords:
        if any(k.lower() in t for k in exclude_keywords):
            return False
    return True

def make_row(source: str, company: str, title: str, location: str, url: str, job_id: str, posted_at: Optional[str]) -> Dict[str, str]:
    return {
        "source": source,
        "company": company,
        "title": title,
        "location": location,
        "url": url,
        "id": job_id,
        "posted_at": posted_at or "",
        "scraped_at": dt.datetime.utcnow().isoformat(timespec="seconds") + "Z",
    }

# -----------------------
# PARSERS PER ATS
# -----------------------
def fetch_lever(company: str) -> List[Dict[str, Any]]:
    # Try Lever public API
    urls = [
        f"https://api.lever.co/v0/postings/{company}?mode=json",
        f"https://api.lever.co/v0/postings/{company}",  # fallback
    ]
    for u in urls:
        data = http_get_json(u)
        if isinstance(data, list):
            out = []
            for j in data:
                title = normalize_text(j.get("text"))
                location = normalize_text(j.get("categories", {}).get("location"))
                hosted_url = normalize_text(j.get("hostedUrl") or j.get("hostedUrlTemplate") or j.get("applyUrl") or j.get("url"))
                job_id = normalize_text(j.get("id") or hosted_url or title)
                posted = j.get("createdAt")
                if posted:
                    try:
                        posted = dt.datetime.utcfromtimestamp(int(posted)/1000).isoformat(timespec="seconds")+"Z"
                    except Exception:
                        posted = None
                out.append({"title": title, "location": location, "url": hosted_url, "id": job_id, "posted_at": posted})
            return out
    return []

def fetch_greenhouse(company: str) -> List[Dict[str, Any]]:
    url = f"https://boards-api.greenhouse.io/v1/boards/{company}/jobs"
    data = http_get_json(url)
    out = []
    if isinstance(data, dict) and isinstance(data.get("jobs"), list):
        for j in data["jobs"]:
            title = normalize_text(j.get("title"))
            # locations may be list or object; Greenhouse returns a dict with 'name'
            loc = ""
            if isinstance(j.get("location"), dict):
                loc = normalize_text(j["location"].get("name"))
            hosted_url = normalize_text(j.get("absolute_url") or "")
            job_id = str(j.get("id") or hashlib.sha1(hosted_url.encode()).hexdigest())
            posted = None
            if j.get("updated_at"):
                posted = j["updated_at"]
            out.append({"title": title, "location": loc, "url": hosted_url, "id": job_id, "posted_at": posted})
    return out

def fetch_smartrecruiters(company: str) -> List[Dict[str, Any]]:
    # Paginates 100 at a time
    base = f"https://api.smartrecruiters.com/v1/companies/{company}/postings"
    out = []
    start = 0
    while True:
        params = {"limit": 100, "offset": start}
        data = http_get_json(base, params=params)
        if not isinstance(data, dict) or "content" not in data or not data["content"]:
            break
        for j in data["content"]:
            title = normalize_text(j.get("name"))
            loc = normalize_text(j.get("location", {}).get("country", ""))
            city = normalize_text(j.get("location", {}).get("city", ""))
            if city:
                loc = f"{city}, {loc}" if loc else city
            url = normalize_text(j.get("ref", {}).get("landingPage"))
            job_id = normalize_text(j.get("id") or url or title)
            posted = j.get("releasedDate")
            out.append({"title": title, "location": loc, "url": url, "id": job_id, "posted_at": posted})
        start += 100
        if start >= int(data.get("totalFound", start)):
            break
    return out

def fetch_workday_json(base_url: str) -> List[Dict[str, Any]]:
    # Workday JSON search endpoint usually supports POST with criteria, but GET often returns first page.
    # We'll try a simple GET first. Advanced: POST with empty body to fetch default listings.
    headers = {"Accept": "application/json"}
    try:
        r = requests.get(base_url, headers=headers, timeout=TIMEOUT)
        r.raise_for_status()
        data = r.json()
    except Exception:
        # Try POST fallback
        try:
            r = requests.post(base_url, headers=headers, json={}, timeout=TIMEOUT)
            r.raise_for_status()
            data = r.json()
        except Exception:
            return []
    out = []
    # Workday v2 returns dict with 'jobPostings' or 'items'
    items = []
    if isinstance(data, dict):
        if isinstance(data.get("jobPostings"), list):
            items = data["jobPostings"]
        elif isinstance(data.get("items"), list):
            items = data["items"]
    for j in items:
        title = normalize_text(j.get("title") or j.get("displayTitle"))
        loc = normalize_text(j.get("locationsText") or j.get("locations", [{}])[0].get("name") if isinstance(j.get("locations"), list) and j.get("locations") else "")
        # URLs are often in 'externalPath' combined with the Workday host
        job_url = ""
        if "externalPath" in j and isinstance(j["externalPath"], str):
            # If base_url is .../jobs, derive host
            m = re.match(r"https?://[^/]+", base_url)
            host = m.group(0) if m else ""
            job_url = f"{host}{j['externalPath']}"
        elif "url" in j:
            job_url = j["url"]
        job_id = normalize_text(str(j.get("id") or j.get("jobPostingId") or job_url or title))
        posted = j.get("postedOn") or j.get("startDate")
        out.append({"title": title, "location": loc, "url": job_url, "id": job_id, "posted_at": posted})
    return out

FETCHERS = {
    "lever": fetch_lever,
    "greenhouse": fetch_greenhouse,
    "smartrecruiters": fetch_smartrecruiters,
    # workday_json handled separately (needs base_url)
}

def dedupe_id(s: str) -> str:
    return hashlib.sha1(s.encode("utf-8")).hexdigest()

def collect_jobs(cfg: Dict[str, Any]) -> List[Dict[str, str]]:
    companies = cfg.get("companies", [])
    rows = []
    for c in companies:
        name = c["name"]
        ats = c["ats_type"].lower()
        include = c.get("title_keywords", [])
        loc_keywords = c.get("location_keywords", [])
        exclude = c.get("exclude_keywords", [])

        jobs = []
        if ats == "workday_json":
            base_url = c.get("base_url")
            if not base_url:
                continue
            jobs = fetch_workday_json(base_url)
        else:
            fetcher = FETCHERS.get(ats)
            if not fetcher:
                continue
            jobs = fetcher(name)

        for j in jobs:
            title = j.get("title", "")
            location = j.get("location", "")
            url = j.get("url", "")
            jid_source = j.get("id") or (title + url)
            jid = dedupe_id(f"{name}|{jid_source}")
            if matches_filters(title, location, include, loc_keywords, exclude):
                rows.append(make_row(ats, name, title, location, url, jid, j.get("posted_at")))
    return rows

def filter_new(rows: List[Dict[str, str]], seen: Dict[str, float]) -> List[Dict[str, str]]:
    new_rows = []
    now = time.time()
    for r in rows:
        jid = r["id"]
        if jid not in seen:
            new_rows.append(r)
            seen[jid] = now
    return new_rows

def write_csv(path: str, rows: List[Dict[str, str]]):
    if not rows:
        return
    fieldnames = ["source", "company", "title", "location", "url", "id", "posted_at", "scraped_at"]
    file_exists = False
    try:
        with open(path, "r", encoding="utf-8") as _:
            file_exists = True
    except FileNotFoundError:
        pass
    with open(path, "a", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        if not file_exists:
            w.writeheader()
        for r in rows:
            w.writerow(r)

def main():
    ap = argparse.ArgumentParser(description="Find marketing jobs from ATS feeds and write to CSV.")
    ap.add_argument("-c", "--config", default="companies.yaml", help="Path to YAML config.")
    ap.add_argument("--once", action="store_true", help="Run once and exit (default).")
    args = ap.parse_args()

    cfg = load_config(args.config)
    seen = load_seen(SEEN_FILE)
    rows = collect_jobs(cfg)
    new_rows = filter_new(rows, seen)
    write_csv(OUTPUT_FILE, new_rows)
    save_seen(SEEN_FILE, seen)

    print(f"Found {len(rows)} matching jobs; {len(new_rows)} new. Wrote to {OUTPUT_FILE}.")
    if not new_rows:
        print("No new matches since last run. Try adjusting keywords or companies.")

if __name__ == "__main__":
    main()
