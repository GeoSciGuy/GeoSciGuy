# Created this file watching a YouTube File
# Corey Schafer : Python Tutorial CSV Module - How to Read, Parse and Write CSV Files
# I am adapting some of the lesson to my environment, I did not download this test data. 
# I am hooking this up directly to my data. 



# Import Area
import csv
import os
import re


# Variables
db_input_folder = r'\\conoco.net\ho_shared\L48 GIS Secure\Land\mherring\automation\python\ndic_daily_permits\db_input'
csv_folder = r'\\conoco.net\ho_shared\L48 GIS Secure\Land\mherring\automation\python\ndic_daily_permits\csv'
count = 0
listofCSVS = os.listdir(csv_folder)
test_file = os.path.join(csv_folder,listofCSVS[0])

listofdbfiles = os.listdir(db_input_folder)
db_file = os.path.join(db_input_folder,listofdbfiles[0])
permitRecord = []

# Regex Patterns
permitNumberRegEx = re.compile(r'#\d\d\d\d\d')

print(db_file)
print(listofdbfiles)
print(listofCSVS)

with open(test_file, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
  
    with open(db_file, 'w') as new_file:
        csv_writer = csv.writer(new_file)
        for line in csv_reader:
            for index, item in enumerate(line):
                print('Index ' + str(index) + ' in line is: ' + item)      
                # if item contains "NORTH DAKOTA INDUSTRIAL COMMISSION" write to Permit Record
                # if item contains "Date:" write to Permit Record
                # if item contains "#\ddddd" write line to permit record
                print('Permit Record so far looks like this: ' + str(permitRecord))

        else:
            print("Done")
            

# Python for Beginners : CSV Parsing ( Part1-2) - "Scott" 
# Really Great Video and a Different Approach

# outfile = open(db_file, 'w' ) 
# outfile_header = "Permit and Company Name , Well Name , Well Legal\n"
# outfile.write(outfile_header)
# with open(test_file, 'r') as infile:
#     reader = csv.reader(infile, delimiter=",")
#     header = next(reader)
#     for row in reader:
        

