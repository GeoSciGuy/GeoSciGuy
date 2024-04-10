# Author :          Matt Herring
# Created Date :    |3-7-2024
# Process Name :    |daily permits automatic gis analysis
# Purporse :        |this script executes the daily gis analysis of daily permit data
###############################################################################

# Setup Enviroment
# Import things
from msilib import init_database
import arcpy
import os
import sys
import traceback
import time


# Set Env Variables for ArcPy
arcpy.env.overwriteOutput = True
arcpy.env.qualifiedFieldNames = False
arcpy.env.parallelProcessingFactor = "95%"
arcpy.env.workspace = r'C:\local_gis\local_gis_sandbox\geodb\local_gis_sandbox.gdb'
arcpy.env.scratchWorkspace = r'C:\local_gis\local_gis_sandbox\geodb\local_gis_sandbox.gdb'


# Set Variables for functions ( Global) 
# copc_leases = r'\\conoco.net\ho_shared\ExplorationBD\Exploration GIS\Automation\connections\osde48p3.sde\RPA.NA_ALL_HDR_LSE'
sde = r'\\conoco.net\ho_shared\L48 GIS Secure\Land\mherring\connections\osde48p3.sde'
ss_path = r'C:\Users\mherrin\OneDrive - ConocoPhillips\gislaunchpad\auto_publish\daily_permits_xlsx'
ss_name = r'daily_permits_gen4.xlsx'
permits_geodb = r'\\conoco.net\ho_shared\L48 GIS Secure\Land\mherring\pro_3_1\daily_permit_auto\daily_permit_auto.gdb'

# Helper Functions
# This script will import the data spreadsheet into a GeoDB. 
# Perform the GIS Analysis

#import the spreadsheet into the GeoDB 
def import_data():
    try:
        input_excel_file = os.path.join(ss_path, ss_name)
        output_table = os.path.join(permits_geodb, 'daily_permits')
        print("Inputs and Outputs" + input_excel_file + output_table)
        arcpy.ExcelToTable_conversion(input_excel_file, output_table)
        print(" daily_permits Created Successfully in geodb")
    except:
        print("Import Data Failed")

# def create_legals_in_table():
#     # this function will create the legals to be used for mapping the section
#     # add columns for section, township and range
#     try:
#         # Add Code Here - add columns
        
#     except:
#         # add code here

# Create a Function that Will Copy the Input Data to a new Table for Manipulation
# def copy_input_data():
#     try: 
#         in_data = r''
#         out_data = r''        
#         arcpy.management.Copy(in_data, out_data)
# Main Program Execution Area
def main():
    start = time.time()
    try:
        # List Functions here
        import_data()
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