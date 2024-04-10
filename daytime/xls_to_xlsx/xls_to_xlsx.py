# Author :          Matt Herring
# Created Date :    |4-1-2024
# Process Name :    |xls_to_xlsx.py
# Purporse :        |converts all xls files in a directory to xlsx file types
###############################################################################

# Setup Enviroment
# Import things
import arcpy
import os
import sys
import traceback
import time
import pandas as pd


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
fc_list = ['L48.L48_LEASES_AOR','L48.L48_NON_EXP_SUB_MLS_AOR','L48.L48_NON_EXP_HDR_ROW_AOR','L48.L48_NON_EXP_HDR_RE_AOR','L48.L48_NON_EXP_HDR_MIN_AOR','L48.L48_NON_EXP_HDR_LSE_AOR','L48.L48_NON_EXP_HDR_LND_AOR']
xls_file_path = r'\\conoco.net\ho_shared\L48 GIS Secure\Land\mherring\projects\ecal'
xlsx_file_path = r'\\conoco.net\ho_shared\L48 GIS Secure\Land\mherring\projects\ecal'
directory = r'\\conoco.net\ho_shared\L48 GIS Secure\Land\mherring\projects\ecal'
file_geodatabase = r'\\conoco.net\ho_shared\L48 GIS Secure\Land\mherring\pro_3_1\ecal_work_\ecal_work_.gdb'
files = os.listdir(directory)
xlsx_files = [file for file in files if file.lower().endswith(".xlsx")]

#function to iterate through the list of fc's in SDE and output CSV files. 
def xlsx_deleter(directory):
    for xlsx_file in xlsx_files:
        file_path = os.path.join(directory, xlsx_file)
        os.remove(file_path)
        print(f"Deleted {xlsx_file}")

    print("All .xlsx files have been deleted.")

def import_xlsx_files_to_geodb(directory):
    for filename in os.listdir(directory):
        if filename.endswith("_new.xlsx"):
            # read the Excel file into a pandas DataFrame
            # df = pd.read_excel(os.path.join(directory, filename))
            # # convert the DataFrame to a table in the File Geodatabase
            # table_name = os.path.splitext(filename)[0]  # remove the .xlsx extension
            # table_name_ = table_name.replace("-","_")
            # arcpy.conversion.ExcelToTable(filename, file_geodatabase)
            print(filename + "Imported")

def convert_all_xls_to_xlsx(directory):
    for filename in os.listdir(directory):
        if filename.endswith(".xls"):
            xls_file_path = os.path.join(directory, filename)
            xlsx_file_path = os.path.join(directory, os.path.splitext(filename)[0] + '.xlsx')
            data_frame = pd.read_html(xls_file_path, index_col=0)[0]
            data_frame.to_excel(xlsx_file_path)
            print(filename + " Converted to XLSX's")

def csv_generator():
    try:
        for i in fc_list:
            print(i)
            in_table = os.path.join(sde, i)
            out_table = os.path.join()
            arcpy.conversion.ExportTable(in_table,)
    except:
        print('well, that didnt work for: ', i)

def sheet_renamer(directory):
    for filename in os.listdir(directory):
    # Check if the file is an Excel file
        if filename.endswith(".xlsx"):
            # Define the path to the Excel file
            excel_file = os.path.join(directory, filename)
            # Load the Excel file
            xls = pd.ExcelFile(excel_file)
            # Get the base name of the file without the extension
            base_name = os.path.splitext(os.path.basename(excel_file))[0].replace('-', '_')
            # Create a new Excel writer object
            writer = pd.ExcelWriter(os.path.join(directory, f"{base_name}_new.xlsx"))
            # Iterate over each sheet in the Excel file
            for sheet_name in xls.sheet_names:
                # Load the sheet into a DataFrame
                df = xls.parse(sheet_name)                
                # Write the DataFrame to the new Excel file with the new sheet name
                df.to_excel(writer, sheet_name=base_name, index=False)
            # Save the new Excel file
            writer.save()
            print('Sheets renamed for ' + filename)

        print(f"All sheets in Excel files in {directory} have been renamed to their respective file names.")

# Main Program Execution Area
def main():
    start = time.time()
    try:
        # csv_generator()
        # convert_xls_to_xlsx('path_to_your_file.xls', 'path_to_your_file.xlsx')
        xlsx_deleter(directory)
        convert_all_xls_to_xlsx(directory)
        sheet_renamer(directory)
        import_xlsx_files_to_geodb(directory)
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