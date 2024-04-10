
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
import pypdf

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
        # print(today)
        # print(target_day)
        # Creating a Date Specific File Name for the NDIC Download
        # Need to create a dynamic string for yesterday.
        # Will use strftime() and Month, Day, Year (%m, %d , %y)

        target_day_fn = 'dr' + target_day.strftime('%m''%d''%y') + '.pdf'
        # print(target_day_fn)
        # Create a download destination file
        # pdf_loc = r'\\conoco.net\ho_shared\L48 GIS Secure\Land\mherring\automation\python\ndic_daily_permits\pdf'
        pdf_loc = r'C:\Users\mherrin\OneDrive - ConocoPhillips\gislaunchpad\auto_publish\daily_permit_reports'
        pdf_fn = target_day_fn
        pdf_file = os.path.join(pdf_loc,pdf_fn)
        # print(pdf_file)
        # res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
        url_base = 'https://www.dmr.nd.gov/oilgas/daily/2024/'
        pdf_fn = target_day_fn
        pdf_dl_url = os.path.join(url_base,pdf_fn)
        res = requests.get(pdf_dl_url)
        res.raise_for_status()
        # this will make the program stop if the above res failes

        local_pdf_file = open(pdf_file,  'wb')
        for chunk in res.iter_content(1000000):
            local_pdf_file.write(chunk)
            local_pdf_file.close
            # print('Local PDF File for Yesterday Created : ' +pdf_fn)
    except:
        pass
# Create the Main Process for Execution    
# Helper function that converts the PDF on Disk to a Txt File. 
def csv_maker():
    # Module Variables
    # pdfPath = r'\\conoco.net\ho_shared\L48 GIS Secure\Land\mherring\automation\python\ndic_daily_permits\pdf'
    pdfPath = r'C:\Users\mherrin\OneDrive - ConocoPhillips\gislaunchpad\auto_publish\daily_permit_reports'
    csvPath = r'\\conoco.net\ho_shared\L48 GIS Secure\Land\mherring\automation\python\ndic_daily_permits\csv'
    txtPath = r'\\conoco.net\ho_shared\L48 GIS Secure\Land\mherring\automation\python\ndic_daily_permits\txt'
    pdfList = []
    listofPDFs = os.listdir(pdfPath)
    listofPDFs.remove('Thumbs.db')
    listofPDFs.sort(key=str.lower)
    # print(listofPDFs)
        # Local Variables
    lenofList = len(listofPDFs)
    
    # Code
    for i in listofPDFs:
        csvFn = os.path.join(csvPath, i[:7]+'.csv')
        pdfFn = os.path.join(pdfPath, i)
        reader = pypdf.PdfReader(pdfFn)
        page = reader.pages[0]
        try: 
            f = open(csvFn,"w")
            f.write(page.extract_text())
            f.close
            f = open(csvFn,"r")
            print(f.read())
            
        except: 
            print("Something went wrong")
            f = open(str(csvFn),"r")
            print(f.read())

        pass

def main():
    try:
        #Calculate Time and Execute Main Program
        startTime = time.time()
        current_ndic_pdf_dl()
        csv_maker()
        endTime = time.time()
        print('It took %s seconds to copy the local pdf and create a CSV.' % (endTime -startTime))
    except:

        pass

# Run the Main Program Process

main()


