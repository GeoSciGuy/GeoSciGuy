import csv
import re

csv_file = r'\\conoco.net\ho_shared\L48 GIS Secure\Land\mherring\automation\python\ndic_daily_permits\csv\dr04282.csv'
csv_results = r'\\conoco.net\ho_shared\L48 GIS Secure\Land\mherring\automation\python\ndic_daily_permits\db_input\test_db_file.csv'
headers = {}
permits = {}

def find_headers():
    
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        data = list(reader)
    regex = r'(PERMITS APPROVED|PERMIT RENEWALS|ADDITIONAL INFORMATION|RELEASED FROM CONFIDENTIAL STATUS|DRY HOLE|TEMPORARILY ABANDONED WELL PLUGGED|PRODUCER NOW ABANDONED|CONFIDENTIAL WELLS PLUGGED OR PRODUCING|DATE|Active Daily Rig Count|APPROVED FOR CONFIDENTIAL STATUS|LOCATIONS RESURVEYED - SURFACE HOLE LOCATION CHANGE|PRODUCING WELL COMPLETED|PRODUCING WELLS COMPLETED|WELL NAME CHANGE)'
    headers = {}
    for i, row in enumerate(data):
        for j, col in enumerate(row):
            match = re.search(regex, col)
            if match:
                headers[match.group()] = {'match': match.group(), 'span': (i,j)}
    print(headers)

def find_permits():
    with open(csv_file, mode='r') as file:
        reader = csv.reader(file)
        data = list(reader)
    for row in data:
        for item in row:
            match = re.search(r'#\d{5}', item)

            if match:
                headers[match.group()] = match.span()

    print(headers)


def main():
    try:
        find_headers()
        find_permits()
        # find_results()
    except:
        print("well, that didnt work")

main()
