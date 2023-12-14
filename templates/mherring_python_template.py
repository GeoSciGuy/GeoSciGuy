# Author :          Matt Herring
# Created Date :    XX-XX-XXXXX
# Process Name :    
# Purporse :        
# Setup Enviroment
# Import things
import arcpy
import os
import sys
import traceback
# Setup Enviroment


# Set Env Variables for ArcPy
arcpy.env.overwriteOutput = True
arcpy.env.qualifiedFieldNames = False
arcpy.env.parallelProcessingFactor = "95%"
arcpy.env.workspace = r'\\conoco.net\ho_shared\L48 GIS Secure\Land\mherring\automation\data\geodb\automation_geodb.gdb'
arcpy.env.scratchWorkspace = r'\\conoco.net\ho_shared\L48 GIS Secure\Land\mherring\automation\data\geodb\automation_scratch.gdb'

# Set Variables for functions ( Global) 
# stg_gdb = r'\\conoco.net\ho_shared\ExplorationBD\Exploration GIS\Automation\python\buffer_analysis\buffer_geodb\buffer_analysis.gdb'
# copc_leases = r'\\conoco.net\ho_shared\ExplorationBD\Exploration GIS\Automation\connections\osde48p3.sde\RPA.NA_ALL_HDR_LSE'
sde = r'\\conoco.net\ho_shared\L48 GIS Secure\Land\mherring\connections\osde48p3.sde'
# list_aut_outputs = [copc_lses_mns_merged,copc_lses_mns_buffer01,copc_lses_mns_buffer02,copc_lses_mns_buffered]
# list_aut_shapes = [exploded_buffer]
shape_folder = r'\\conoco.net\ho_shared\L48 GIS Secure\Land\mherring\automation\data\shps'
# r'\\conoco.net\ho_shared\Spotfire\Projects\Lower 48 Land\GLASS\geodb'

# Begin Code Section
# Attempt Cleaning of Pre-Existing Data
# Module that Merges the Leases and Minerals from SDE
# def merge_lses_mns():
#     # Code Block
#     try:
#         arcpy.Merge_management([copc_leases, copc_minerals],copc_lses_mns_merged)
#         print("Merge Successful")
#         # print(str(copc_leases))
#         # print(str(copc_minerals))
#     except:
#         print('Merge Failed')
#         # print(str(copc_leases))
#         # print(str(copc_minerals))
#         print(arcpy.GetMessages())
#         pass

# def buffer_generation():
#     try:
#         arcpy.MultipleRingBuffer_analysis(copc_lses_mns_merged, copc_lses_mns_buffer01, "1;2;3", "Miles", "distance", "ALL", "OUTSIDE_ONLY")
#         print('Buffers created successfully')
#     except:
#         print('Buffer Creation Failed')
#         pass

# This function deletes the fc's created by previous runs of this script.
# def delete_previous():
#     # for each fc in the list of fc's
#     for i in list_aut_outputs:
#         print(i)
#         if arcpy.Exists(i):
#             arcpy.Delete_management(i)
#             print(i + ' was successfully deleted.')
#         else:
#             print(i + ' Did not exist' )
#             pass
    
# Explode the Buffer into all the pieces. 
# def buffer_exploder():
#     try:
#         # arcpy.MultipartToSinglepart_management(copc_lses_mns_buffer01,exploded_buffer)
#         print(arcpy.GetMessages())
#         print('Exploder Worked, Yahoo!')
#     except:
#         print(arcpy.GetMessages())
#         print('Crap, Exploder blew up!')
#         pass

# Shapefile Maker 
# def shapefile_maker():
#     try:
#         # arcpy.FeatureClassToShapefile_conversion(list_aut_shapes,shape_folder)
#         print(arcpy.GetMessages())
#         print("Shapefile Created Successfully!")
#     except:
#         print(arcpy.GetMessages())
#         print("Dangit Batman, Shapefile Creation Failed!!")
#         pass

# Main Program Execution Area
def main():
    try:
        # delete_previous()
        # merge_lses_mns()
        # buffer_generation()
        # buffer_exploder()
        # shapefile_maker()
        print('Main Execution is complete')
    except:
        print('Main Failed.....back to the drawing board')
        print(arcpy.GetMessages())
        pass

# main()