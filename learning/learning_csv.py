import csv
import os
import datetime
import pypdf

# Text File and Related
# Path to the Text Files I am working with. 
txt_path = r"\\conoco.net\ho_shared\L48 GIS Secure\Land\mherring\automation\python\ndic_daily_permits\txt"
txt_fn = r'pdf_text.txt'
# Path where PDF Related things are stored for this script
pdf_path = r'\\conoco.net\ho_shared\L48 GIS Secure\Land\mherring\automation\python\ndic_daily_permits\pdf'
# PDF File Names found here. 
# This is the PDF used to develop this script. Hard Coding for now. Will make dynamic later
pdf_fn = r'dr020623.pdf'

pdfFile = os.path.join(pdf_path, pdf_fn)
textFile = os.path.join(txt_path,txt_fn)

# Testing the outputs
print("Current PDF File: " + ' ' + pdfFile) 
print('Current Text File: ' + ' ' + textFile)


# working with the PDF to generate the CSV
# Open the PDF File in Read and Binary Mode. 
pdfFileObj = open(pdfFile, 'rb')
# Call the PdfReader and Pass it the pdfFileObj
pdfReader = pypdf.PdfReader(pdfFileObj)
print('pdfFileObj and pdfReader have been created.')
print(len(pdfReader.pages))
# create an object for the page, To extract text from a page,
#  you need to get a Page object, which represents a single page of a PDF,
#  from a PdfFileReader object. You can get a Page object by calling the getPage() method 
pageObj = pdfReader.pages[0]
pageObj.extract_text()
print('Now we are ready to write the text to a textfile')
textFileObj = open(textFile,'w')
textFileObj.write(pageObj.extract_text())
pdfFileObj.close
textFileObj.close
print('closed both pdf and txt files')






    
# General Notes Researched and used in Scripting here. 
# Open Structure in Python Language Reference
# open(file, mode='r', buffering=- 1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
### Text File Mode! ###
# Character  	Meaning
# 'r'		open for reading (default)
# 'w'		open for writing, truncating the file first
# 'x'		open for exclusive creation, failing if the file already exists
# 'a'		open for writing, appending to the end of file if it exists
# 'b'		binary mode
# 't'		text mode (default)
# '+'		open for updating (reading and writing)