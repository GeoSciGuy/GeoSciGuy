# Import Area
import pypdf
import os 

# Variable Area
workingfolder = r'C:\Dev_Source\github_repos\GeoSciGuy\learning\pdf_files'
pdf_in_fn = r'dr013123.pdf'

pdfFileObj = open((os.path.join(workingfolder, pdf_in_fn)),'rb')
pdfReader = pypdf.PdfFileReader(pdfFileObj)

