# Author :          |Matt Herring
# Created Date :    |8/24/2023
# Process Name :    |nightly_aor_data_csv_generator.py
# Purporse :        |Generate CSV's for SDE Layers of Corp Data SJ To AOR
###############################################################################

# Setup Enviroment
# Import things
import arcpy
import os
import sys
import traceback
import time

# Set Env Variables for ArcPy
arcpy.env.overwriteOutput = True
arcpy.env.qualifiedFieldNames = False
arcpy.env.parallelProcessingFactor = "95%"
arcpy.env.workspace = r'\\conoco.net\ho_shared\L48 GIS Secure\Land\mherring\automation\pro\automation\automation.gdb'
arcpy.env.scratchWorkspace = r'\\conoco.net\ho_shared\L48 GIS Secure\Land\mherring\automation\data\geodb\automation_scratch.gdb'

# Set Variables for functions ( Global) 
# copc_leases = r'\\conoco.net\ho_shared\ExplorationBD\Exploration GIS\Automation\connections\osde48p3.sde\RPA.NA_ALL_HDR_LSE'
sde = r'\\conoco.net\ho_shared\L48 GIS Secure\Land\mherring\connections\osde48p3.sde'
csv_folder = r'\\conoco.net\ho_shared\L48 GIS Secure\Land\mherring\automation\python\nightly_aor_export_csv\csv'
fc_list = ['L48.L48_LEASES_AOR','L48.L48_NON_EXP_SUB_MLS_AOR','L48.L48_NON_EXP_HDR_ROW_AOR','L48.L48_NON_EXP_HDR_RE_AOR','L48.L48_NON_EXP_HDR_MIN_AOR','L48.L48_NON_EXP_HDR_LSE_AOR','L48.L48_NON_EXP_HDR_LND_AOR']

#function to iterate through the list of fc's in SDE and output CSV files. 
def csv_generator():
    try:
        for i in fc_list:
            print(i)
            in_table = os.path.join(sde, i)
            out_table = os.path.join(csv_folder,i +'.csv')
            print(out_table)
            arcpy.conversion.ExportTable(in_table,out_table)
            print(i,' completed successfully!')
    except:
        print('well, that didnt work for: ', i)

# Main Program Execution Area
def main():
    start = time.time()
    try:
        csv_generator()
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