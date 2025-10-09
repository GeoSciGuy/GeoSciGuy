# Created by : Matthew Herrinng
# Created on : 2025-10-07   
# Process    : NDIC Data Engineering
# File Name  : ndic_data_engineering.py
# Description: This script is designed to handle data engineering tasks for the NDIC regulatory agency.
#              It includes functions for data extraction, transformation, and loading (ETL) processes.
#              The script is modular and can be expanded with additional functionalities as needed.
# License    : Not Licensed for public use.             
#               (c) Copyright 2025 Matthew Herrinng
#              All rights reserved.
#              Unauthorized copying of this file, via any medium is strictly prohibited.
#              Proprietary and confidential.
###############################################################################################################

# Import Area
import os
import time
import sys
import datetime
import requests
import pdfplumber
import re
from pathlib import Path
from collections import defaultdict

# Variables Area
# Workflow Description
# 1. Data Extraction: Connect to NDIC data sources and extract relevant datasets to local storage.
# Time related variables and logic below. 
ndic_daily_permit_url = "https://www.dmr.nd.gov/oilgas/daily/"
today = datetime.date.today()
current_year = today.year
yyyy = current_year
current_month = today.month
yy = str(current_year)[-2:]
current_day = today.day
mm = f"{current_month:02d}"  # Ensures two-digit month format
formatted_date = today.strftime("%Y%m%d")
day_adjusted = current_day - 1  # Adjusting day for data availability
day_str = f"{day_adjusted:02d}"   # -> "03"
permit_fn = "dr" + str(mm) + str(day_str) + str(yy) + ".pdf"
permit_report_dl_url = os.path.join(ndic_daily_permit_url,str(yyyy), permit_fn)
# Note: The above filename format is based on the assumption that the files are named in a specific pattern.
# Adjust the pattern as necessary based on actual file naming conventions.

# I want to print base url, permit_fn, download_url variables to ensure they are correct.
# print("Base URL:", ndic_daily_permit_url)
# print("Permit Filename:", permit_fn)
# print("Download URL:", permit_report_dl_url)

local_dl_folder = "/Users/matthewherring/automation/north_dakota/ndic/downloads"

def download_permit_pdf(download_url, local_folder):
    try:
        response = requests.get(download_url, stream=True)
        response.raise_for_status()
        os.makedirs(local_folder, exist_ok=True)
        local_path = os.path.join(local_folder, os.path.basename(download_url))
        with open(local_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        print(f"Downloaded PDF to: {local_path}")
        return local_path
    except Exception as e:
        print(f"Failed to download PDF: {e}")
        return None
    
# Text Parsing Function to extract permit data from PDF
CATEGORY_LABELS = [
    "PERMITS APPROVED:",
    "ADDITIONAL INFORMATION:",
    "APPROVED FOR CONFIDENTIAL STATUS:",
    "RELEASED FROM “CONFIDENTIAL” STATUS:",
    "CONFIDENTIAL WELLS PLUGGED OR PRODUCING:",
    "PRODUCING WELLS COMPLETED:",
    "SWD PERMIT:",

    # add more when you discover them
]
PERMIT_PATTERN = re.compile(r"#\d+")
pdf_path = Path(local_dl_folder) / permit_fn

def parse_permits_by_category(pdf_path: str) -> dict[str, list[str]]:
    grouped = defaultdict(list)
    current_category = None

    with pdfplumber.open(pdf_path) as pdf:
        page = pdf.pages[0]                  # extend to multiple pages if needed
        for raw_line in page.extract_text().splitlines():
            line = raw_line.strip()

            # check for a new category label
            if any(line.startswith(label) for label in CATEGORY_LABELS):
                current_category = next(label for label in CATEGORY_LABELS if line.startswith(label))
                continue

            if current_category:
                permits = PERMIT_PATTERN.findall(line)
                if permits:
                    grouped[current_category].extend(permits)
                # optionally store the entire line or other fields along with the permit id

    return grouped




# 2. Convert downloaded data to usable formats for analysis.
# 3. Begin the process of extracting information from the usable data. 
# Helper FUnctions









# Main Function
def main():
    try:
        start = time.perf_counter()
        print("Base URL:", ndic_daily_permit_url)
        print("Permit Filename:", permit_fn)
        print("Download URL:", permit_report_dl_url)
        download_permit_pdf(permit_report_dl_url, local_dl_folder)
        parse_permits_by_category(str(pdf_path))
        grouped_permits = parse_permits_by_category(str(pdf_path))
        print(grouped_permits)
        elapsed = time.perf_counter() - start
        print(f" Main Succeeded and the time elapsed: {elapsed:.3f} seconds")
    except Exception as e:
        print("An error occurred:", e)
        elapsed = time.perf_counter() - start
        print(f" Main Failed and the time elapsed: {elapsed:.3f} seconds")
    finally:
        print("Execution completed.")
        

main()
