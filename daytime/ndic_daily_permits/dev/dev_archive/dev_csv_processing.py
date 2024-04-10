# Purpose : To create a module that will process each CSV file for the next 
# step of the Daily Permit Solution. 

# Import Area ##########################################
import csv
import re
import pandas
import os 



# Variable Area
csv_folder = r'\\conoco.net\ho_shared\L48 GIS Secure\Land\mherring\automation\python\ndic_daily_permits\csv'
count = 0
listofCSVS = os.listdir(csv_folder)

# Helper Function Area
def csv_processor():
    try:
        print("There are " + (str(len(listofCSVS))) + " csv's to process")
        count =(str(len(listofCSVS)))
        print(count)
        for i in listofCSVS:
            csvfilepath = os.path.join(csv_folder,i)
            print("Here we go, processing: " + csvfilepath)
            file = open(csvfilepath)
            csvfileLine = file.readlines()
            print("Checking out this line: --" + (str(csvfileLine)))
            file.close
    except:
        print("Womp Womp...try again")
        file.close
        return


# Main program Area
def main():
    try:
        csv_processor()
    except: 
        print("Well that failed - Main")

main()