# Code was created 2-27-2023
# Author : Matt Herring
# Implemented : 2-27-2023
# Added to Daily Permit PDF Script already running Daily. 


# Code to convert PDF's to CSV's
# Import Area
import csv
import pypdf
import os
import pypdf

# Global Variables Areas
pdfPath = r'\\conoco.net\ho_shared\L48 GIS Secure\Land\mherring\automation\python\ndic_daily_permits\pdf'
csvPath = r'\\conoco.net\ho_shared\L48 GIS Secure\Land\mherring\automation\python\ndic_daily_permits\csv'
txtPath = r'\\conoco.net\ho_shared\L48 GIS Secure\Land\mherring\automation\python\ndic_daily_permits\txt'
pdfList = []
listofPDFs = os.listdir(pdfPath)
listofPDFs.remove('Thumbs.db')
listofPDFs.sort(key=str.lower)
print(listofPDFs)

# csv related things

# Helpder Functions
def csv_maker():
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
        


# Main Functions
csv_maker()

