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



# generate the URL to download yesterdays pdf
# helper functions
def current_ndic_pdf_dl():
    try:
        # Algorithm for Scripting
        # Create a datetime for yesterday
        # Create a Timedelta for one day. 
        today = datetime.datetime.now()
        days = datetime.timedelta(days=1)
        target_day = today - days
        print(today)
        print(target_day)
        # Creating a Date Specific File Name for the NDIC Download
        # Need to create a dynamic string for yesterday. 
        # Will use strftime() and Month, Day, Year (%m, %d , %y)
        target_day_fn = 'dr' + target_day.strftime('%m''%d''%y') + '.pdf'
        print(target_day_fn)
        # Create a download destination file
        pdf_loc = 'C:\Dev_Source\github_repos\GeoSciGuy\pdf_files'
        pdf_fn = target_day_fn
        pdf_file = os.path.join(pdf_loc,pdf_fn)
        print(pdf_file)

        # res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
        url_base = 'https://www.dmr.nd.gov/oilgas/daily/2023/'
        pdf_fn = target_day_fn
        pdf_dl_url = os.path.join(url_base, pdf_fn)
        res = requests.get(pdf_dl_url)
        res.raise_for_status() # this will make the program stop if the above res failes
        local_pdf_file = open(pdf_file,  'wb')
        for chunk in res.iter_content(1000000):
            local_pdf_file.write(chunk)
        local_pdf_file.close
        print('Local PDF File for Yesterday Created : ' + pdf_fn)
    except:
        pass

# Create the Main Process for Execution    
def main():
    try:
        #Calculate Time and Execute Main Program
        startTime = time.time()
        current_ndic_pdf_dl()
        endTime = time.time()
        print('It took %s seconds to copy the local pdf.' % (endTime - startTime))
    except:
        pass

# Run the Main Program Process
main()
