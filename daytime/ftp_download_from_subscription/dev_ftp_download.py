# Author :          Matt Herring
# Created Date :    |10/30/2023
# Process Name :    |ftp_data_downloader
# Purporse :        |download subscription updates from various data vendors at COPC
###############################################################################

# Setup Enviroment
# Import things
import arcpy
import os
import sys
import traceback
import time
import ftplib

# Set Env Variables for ArcPy
arcpy.env.overwriteOutput = True
arcpy.env.qualifiedFieldNames = False
arcpy.env.parallelProcessingFactor = "95%"
arcpy.env.workspace = r'\\conoco.net\ho_shared\L48 GIS Secure\Land\mherring\automation\pro\automation\automation.gdb'
arcpy.env.scratchWorkspace = r'\\conoco.net\ho_shared\L48 GIS Secure\Land\mherring\automation\data\geodb\automation_scratch.gdb'

# Set Variables for functions ( Global) 
# copc_leases = r'\\conoco.net\ho_shared\ExplorationBD\Exploration GIS\Automation\connections\osde48p3.sde\RPA.NA_ALL_HDR_LSE'
sde = r'\\conoco.net\ho_shared\L48 GIS Secure\Land\mherring\connections\osde48p3.sde'
shape_folder = r'\\conoco.net\ho_shared\L48 GIS Secure\Land\mherring\automation\data\shps'
# fc_list = ['L48.L48_LEASES_AOR','L48.L48_NON_EXP_SUB_MLS_AOR','L48.L48_NON_EXP_HDR_ROW_AOR','L48.L48_NON_EXP_HDR_RE_AOR','L48.L48_NON_EXP_HDR_MIN_AOR','L48.L48_NON_EXP_HDR_LSE_AOR','L48.L48_NON_EXP_HDR_LND_AOR']


# Function for FTP Connection and File Download. 
def ftp_file_getter():
    # Connect to the FTP server
    ftp = ftplib.FTP("ftp://ftga.ihs.com")
    ftp.login("conocophillips_matthew_herring", "IH@tePasswords!2o23")

    # Navigate to the directory containing the files you want to download
    ftp.cwd("/US_LAND_DATA/NATIONWIDE_ALL_EXC_PAOHWV")

    # Download the files
    filename = "example.txt"
    with open(filename, "wb") as file:
        ftp.retrbinary(f"RETR {filename}", file.write)

    # Close the connection
    ftp.quit()
# Main Program Execution Area
def main():
    start = time.time()
    try:
        # Function Calls go here.
        print('Main Execution is complete')
        print(arcpy.GetMessages())
    except:
        print('Main Failed.....back to the drawing board')
        print(arcpy.GetMessages())
        pass
    end = time.time()
    print('Main execution time : ',  ((((end-start) * 10**3) / 1000)/60) ,"Minutes")
    print(os.getlogin() + '- Main Execution is complete')

# Run the main function here. 
main()


# Notes
# ArcPy - Export Table Python Syntax
# arcpy.conversion.ExportTable(in_table, out_table,
#  {where_clause}, use_field_alias_as_name, {field_mapping}, {sort_field})

#FTP_Library Doc
# class ftplib.FTP(host='', user='', passwd='', acct='', timeout=None,
#  source_address=None, *, encoding='utf-8')
# https://docs.python.org/3/library/ftplib.html
