# Author :          Matt Herring
# Created Date :    04-19-2022
# Process Name :    ana_per_rig_sj_lse_2022
# Purporse :        Spatial Join, Rigs and Permits to COPC Leases
#########################################################################################################################

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
arcpy.env.workspace = r'\\conoco.net\ho_shared\L48 GIS Secure\Land\mherring\automation\data\geodb\automation_geodb.gdb'
arcpy.env.scratchWorkspace = r'\\conoco.net\ho_shared\L48 GIS Secure\Land\mherring\automation\data\geodb\automation_scratch.gdb'

# Set Variables for functions ( Global) 
# stg_gdb = r'\\conoco.net\ho_shared\ExplorationBD\Exploration GIS\Automation\python\buffer_analysis\buffer_geodb\buffer_analysis.gdb'
copc_lses_sj_permits = r'\'
copc_leases = r'\RPA.NA_ALL_HDR_LSE'
sde = r"\\conoco.net\ho_shared\L48 GIS Secure\Land\mherring\connections\osde48p3.sde"
list_aut_outputs = ['copc_lses_sj_permits','copc_lses_sj_rigs']
# list_aut_shapes = [exploded_buffer]
shape_folder = r'\\conoco.net\ho_shared\L48 GIS Secure\Land\mherring\automation\data\shps'
# r'\\conoco.net\ho_shared\Spotfire\Projects\Lower 48 Land\GLASS\geodb'

# Begin Code Section
# This function deletes the fc's created by previous runs of this script.
def delete_previous():
     # for each fc in the list of fc's
     for i in list_aut_outputs:
         print(i)
         if arcpy.Exists(i):
             arcpy.Delete_management(i)
             print(i + ' was successfully deleted.')
         else:
             print(i + ' Did not exist' )
             pass

# Create layer files for geoprocessing
# Perform Spatial Join of Permits to COPC Leases
# Perform Spatial Join of Rigs to COPC Leases

# Main Program Execution Area
def main():
    try:
        # delete_previous()

        print('Main Execution is complete')
    except:
        print('Main Failed.....back to the drawing board')
        print(arcpy.GetMessages())
        pass

# main()
