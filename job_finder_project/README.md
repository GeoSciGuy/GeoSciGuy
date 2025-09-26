# Marketing Job Finder (ATS Feeds)

A simple Python script that checks public job board endpoints for multiple ATS platforms and writes matched roles to a CSV.

## What this does
- Polls **Lever**, **Greenhouse**, **SmartRecruiters**, and **Workday JSON** job endpoints.
- Filters by **title keywords**, optional **location keywords**, and **exclusions**.
- Saves results to `jobs_latest.csv` and keeps a cache (`.seen_jobs.json`) so you only see **new** roles.

## Quick Start (macOS / VS Code)
1. Ensure you have Python 3.10+ installed:  
   ```bash
   python3 --version
   ```
2. Create a virtual env and install deps:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```
3. Edit `companies.yaml` — replace example slugs with real company slugs and tweak keywords.
4. Run it:
   ```bash
   python job_finder.py --once
   ```
   This writes matches to `jobs_latest.csv`. Open it in Numbers/Excel.

## Scheduling (optional)
- macOS **launchd** or **cron** can run it daily. Example cron (runs at 8:10am):
  ```cron
  10 8 * * * /bin/bash -lc 'cd /home/sandbox && source .venv/bin/activate && python job_finder.py --once'
  ```

## Notes
- **LinkedIn**: This script avoids scraping LinkedIn to comply with their terms. Use LinkedIn for alerts/visibility.
- **Workday**: You must provide the correct JSON endpoint in `companies.yaml` for each Workday company you track.
- If a company changes their career site structure, update the config accordingly.

## Output fields
- source (ATS type), company, title, location, url, id, posted_at (if available), scraped_at

## Uninstall / cleanup
- Delete the project folder. The script only writes `jobs_latest.csv` and `.seen_jobs.json` in the same directory.
