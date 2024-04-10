# Author :          Matt Herring                                                      #
# Created Date :    01-30-2023                                                        #
# Process Name :    ndic_daily_permit_exam                                            #
# Purporse :        auto manange daily report for ndic permits                        #
# Python Version:   3.6                                                               #
#######################################################################################

# Setup Enviroment
# Import things

### standard lbrary things
### Previously Used Sitepackages ###
# import sys
# import traceback
# import urllib.request
# import zipfile
import os
import time
import datetime
import pypdf
import requests

# ## Third Party
# GIS Things
import arcpy

# Set Env Variables for ArcPy
arcpy.env.overwriteOutput = True
arcpy.env.qualifiedFieldNames = False
arcpy.env.parallelProcessingFactor = "96%"
# arcpy.env.workspace = r'\\conoco.net\ho_shared...'
# arcpy.env.scratchWorkspace = r'\\conoco.net\ho_shared'

# Set Variables for functions ( Global)

##### Begin Code Section #####
### Funtion that Builds the File Name and Creates the Today.txt File. 
def today_maker():
    try:
        # Variables for Date Time ( File Name Creation)
        pdf_url = r'https://www.dmr.nd.gov/oilgas/daily/2023/'
        init_time = datetime.datetime.now()
        month = init_time.strftime('%m')
        day = init_time.strftime('%d')
        year = init_time.strftime('%y')
        yesterday = (init_time + datetime.timedelta(days=-1)).strftime("%d")
        today_fn = "dr" + month + day + year + ".pdf"
        yesterday_fn = "dr" + month + yesterday + year + ".pdf"
        yesterday_url = pdf_url + yesterday_fn
        ### Code to test outputs ###
        # print((init_time.strftime('%m')),(init_time.strftime('%d')), ((init_time.strftime('%y'))))
        # print(today_fn)
        # print(yesterday_fn)
        # print(pdf_url + today_fn)
        print(pdf_url + yesterday_fn) # Answer
        print(yesterday_url) # Output should be the same
        # Variables for Text File Stored Locally
        txt_path = r'\\conoco.net\ho_shared\L48 GIS Secure\Land\mherring\automation\python\ndic_daily_permits\txt'
        txt_file = r'today.txt'
        txt_fn = os.path.join(txt_path,txt_file)
        # test_fn = r"\\conoco.net\ho_shared\L48 GIS Secure\Land\mherring\automation\python\ndic_daily_permits\pdf\dr012723.pdf"
        # PDF Reader Variables
        yesterday_pdf = requests.get(yesterday_url)
        reader = pypdf.PdfReader(yesterday_pdf)
        page = reader.pages[0]
        print(page.extract_text())
        f = open (txt_fn,"wb")
        f.write(page.extract_text())
        f.close
        print("All Done")

    except:
        print("Except Reached")
        pass


# Open PDF
# def pdf_processing():
#     try:   
#         print(page.extract_text())
#         f = open (txt_fn,"w")
#         f.write(page.extract_text())
#         f.close
#     except:
#         print("something went wrong")
#         pass

### Defined Functions here###
def main_process():
    try: 
        # Helper Proess Name here
        # pdf_processing()
        today_maker()
    except: 
        # Alternative Process Here
        pass

# Main Program Execution Area
def main():
    start = time.time()
    try:
        main_process()
        print(os.getlogin() + '- Main Execution is complete')
    except:
        print('Main Failed.....back to the drawing board')
        print(arcpy.GetMessages())
        pass
    end = time.time()
    print('The time of execution for process input data was : ',  ((end-start) * 10**3) / 1000 ,"seconds")
    print('Main execution time : ',  ((((end-start) * 10**3) / 1000)/60) ,"Minutes")

main()