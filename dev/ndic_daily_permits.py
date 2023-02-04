# Author : Matt Herring
# Script : ndic_daily_permits.py
# Purpose : This script downloads the daily NDIC Permits
#           and copies them locally. 
#           Additional Processing if possible. 

# Imports
import datetime
import requests
import os
import time

# Algorithm for Scripting
# Create a datetime for yesterday
# Create a Timedelta for one day. 
today = datetime.datetime.now()
one_day = datetime.timedelta(days=1)
yesterday = today - one_day
print(today)
print(yesterday)

# Creating a Date Specific File Name for the NDIC Download
# Need to create a dynamic string for yesterday. 
# Will use strftime() and Month, Day, Year (%m, %d , %y)
yesterday_fn = 'dr' + yesterday.strftime('%m''%d''%y') + '.pdf'

# generate the URL to download yesterdays pdf
# helper functions
def current_ndic_pdf_dl():
    try:
        # Create a download destination file
        pdf_loc = 'C:\Dev_Source\github_repos\GeoSciGuy\learning\dl'
        pdf_fn = 'current_ndic.pdf'
        pdf_file = os.path.join(pdf_loc,pdf_fn)
        print(pdf_file)

        # res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
        url_base = 'https://www.dmr.nd.gov/oilgas/daily/2023/'
        pdf_fn = yesterday_fn
        pdf_dl_url = os.path.join(url_base, pdf_fn)
        res = requests.get(pdf_dl_url)
        res.raise_for_status() # this will make the program stop if the above res failes
        local_pdf_file = open(pdf_file,  'wb')
        for chunk in res.iter_content(1000000):
            local_pdf_file.write(chunk)
        local_pdf_file.close
    except:
        pass

# Create the Main Process for Execution    
def main():
    try:
        #Calculate Time and Execute Main Program
        startTime = time.time()
        current_ndic_pdf_dl
        endTime = time.time()
        print('Took %s seconds to calculate.' % (endTime - startTime))
    except:
        pass