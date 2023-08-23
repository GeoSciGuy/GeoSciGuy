# Author :          Matt Herring
# Created Date :    08-23-2023
# Process Name :    NDIC Daily Data Getter
# Purporse :        The purpose of this module is to download NDIC Data Daily for Anaylysis

# Setup Enviroment
# Import things
import arcpy
import os
import sys
import traceback

# Set Env Variables for ArcPy
arcpy.env.overwriteOutput = True
arcpy.env.qualifiedFieldNames = False
arcpy.env.parallelProcessingFactor = "95%"
arcpy.env.workspace = r'C:\gis_local\bakken_ndic_data\bakken_ndic_data.gdb'
arcpy.env.scratchWorkspace = r'C:\gis_local\data\scratch\scratch.gdb'

# Set Variables for functions ( Global) 
# sde = r'' # Need to setup a local SDE Server first then I can use this variable. 
shape_folder = r'C:\gis_local\bakken_ndic_data\shapes'

# Begin Code Section

# Main Program Execution Area
def main():
    try:
        # As Modules are created, list them here to include them in program execution. 
        print('Main Execution is complete')
    except:
        print('Main Failed.....back to the drawing board')
        print(arcpy.GetMessages())
        pass

# When you are ready to schedule this script to run, uncomment the following line. 
# main()