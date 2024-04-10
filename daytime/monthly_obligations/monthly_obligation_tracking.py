# Author :          Matt Herring                                                      #
# Created Date :    11-15-2022                                                        #
# Process Name :    monthly obligation tracking                                       #
# Purporse :        executes workflow for producing the monthly obligations report    #
# Python Version:   3.6                                                               #
#######################################################################################

# Setup Enviroment
# Import things

### standard lbrary things
import os
import sys
import traceback
import urllib.request
import zipfile
# ## Third Party
import pandas
import numpy
# GIS Things
import arcpy

# Set Env Variables for ArcPy
arcpy.env.overwriteOutput = True
arcpy.env.qualifiedFieldNames = False
arcpy.env.parallelProcessingFactor = "96%"
# arcpy.env.workspace = r'\\conoco.net\ho_shared...'
# arcpy.env.scratchWorkspace = r'\\conoco.net\ho_shared'

# Set Variables for functions ( Global)
datapath = r'\\HOCTCVMWX022\gis_local$\Analysis\monthly_obligations\pro\obligations.gdb'
# shppath = os.path.join(datapath,r'shp')
gdbpath = os.path.join(datapath,r'obligations.gdb')
# url = "https://gis.dmr.nd.gov/downloads/oilgas/shapefile/"
lst = ['OGD_CasesDocketed']
gdbprefix = "aut_mgh_moe"

# Begin Code Section

# Template for Stored Procedures
# def procedure_name():
#     # for each fc in the list of fc's
#     for i in list:
#         print(i)
#         if arcpy.Exists(i):
#             arcpy.Delete_management(i)
#             print(i + ' was successfully deleted.')
#         else:
#             print(i + ' Did not exist' )
#             pass


# Main Execution Section
main()