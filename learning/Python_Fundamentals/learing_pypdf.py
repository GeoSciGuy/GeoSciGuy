from pypdf import PdfReader
import os

fn = r"\\conoco.net\ho_shared\L48 GIS Secure\Land\mherring\automation\python\ndic_daily_permits\pdf\dr020623.pdf"
reader = PdfReader(fn)
page = reader.pages[0]
print(page.extract_text())

txt_path = r'\\conoco.net\ho_shared\L48 GIS Secure\Land\mherring\automation\python\ndic_daily_permits\txt'
txt_file = r'db_input.txt'
txt_fn = os.path.join(txt_path,txt_file)

print(txt_fn)

def txt_file_maker():
    try: 
        f = open(txt_fn,"w")
        f.write(page.extract_text())
        f.close
        f = open(txt_fn,"r")
        print(f.read())
        
    except: 
        print("Something went wrong")
        f = open(str(txt_fn),"r")
        print(f.read())

    pass

# I would like to make an array
# how do I do it? 


my_list = [1, 2, 3, 4, 5]
# txt_file_maker()


# from pypdf import PdfReader

# reader = PdfReader("example.pdf")
# number_of_pages = len(reader.pages)
# page = reader.pages[0]
# text = page.extract_text()

import pypdf

reader = PdfReader(txt_fn)
num_of_pages = len(reader.pages)
page = reader.pages[0]
text = page.extract_text()
