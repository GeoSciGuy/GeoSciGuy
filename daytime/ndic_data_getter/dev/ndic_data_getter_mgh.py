# Author :          Matt Herring                                                      #
# Created Date :    03-30-2022                                                        #
# Process Name :    ndic_data_getter                                                  #
# Purporse :        atuomatically download several shape files from the NDIC website  #
# Python Version:   3.6                                                               #
#######################################################################################

# Setup Enviroment
# Import things
import arcpy
import os
import sys
import traceback
# import urllib.request from urllib
import urllib
import zipfile
### standard lbrary modules
# import urllib2
# import zipfile
# import os
# ## Third Party
# import arcpy

# Set Env Variables for ArcPy
arcpy.env.overwriteOutput = True
arcpy.env.qualifiedFieldNames = False
arcpy.env.parallelProcessingFactor = "95%"
# arcpy.env.workspace = r'\\conoco.net\ho_shared...'
# arcpy.env.scratchWorkspace = r'\\conoco.net\ho_shared'

# Set Variables for functions ( Global)
datapath = r'\\conoco.net\ho_shared\RBU_GIS_SECURE\greater_williston\data'
shppath = os.path.join(datapath,r'shp\ndic')
gdbpath = os.path.join(datapath,r'gdb\rbu_gw_principal_fgdb.gdb')
url = "https://www.dmr.nd.gov/output/ShapeFiles/"
#lst = ['BLMLands','CasesDocketed','CityBoundaries','CountyRoads','Directionals','DrillingSpacingUnits','FederalForestService','FortBerthold_Surface','GasPlants','Horizontals_Lines','MajorRivers','MajorRoads','NDLandDept','OilFields','PermitStatusBeforeSpud','Reservations','UnitBoundaries','Wells']
lst = ['BLMLands','CasesDocketed','CityBoundaries','CountyBoundaries','CountyRoads','Directionals','Directionals_Lines','DrillingSpacingUnits','FederalForestService','FedForestService','FortBerthold_Mineral','FortBerthold_Surface','GasPlants','Horizontals','Horizontals_Lines','InspectorAreas','MajorRivrs','MajorRoads','MissouriRiver','NDLandDept','OilFields','PermitStatusBeforeSpud','Reservations','Rigs','Sections','Seismic2DPreplot','Seismic3DPreplot','Townships','UnitBoundaries','Wells',]
gdbprefix = "rbu_gw_ndic_"

# Begin Code Section
# Attempt Cleaning of Pre-Existing Data

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


def main_process():
    # Iterate through each Named Shape in the List (i). 
    for i in lst:
        # create a variable zip, and use urllib to open the URL
        print('Beginning processing for ' + i)
        zip = urllib.request.urlopen(url+i+".zip",)
        # read the zip file after urllib has opened the link
        with open(os.path.join(shppath,i+".zip"),'wb') as output:
            # read the zip file into memory for additional processing
            output.write(zip.read()) 
    
    # Create a zipfile variable and assign it the currently handled 'i'
    print('i' + 'successfully read from website, beginning zipfile creation')
    zfile = zipfile.ZipFile(os.path.join(shppath,i+".zip"),'r')
    # Extract the Current 'i' zipfile
    zfile.extractall(os.path.join(shppath))
    
    # Close the currently being read zip file, best practice here. 
    zipfile.ZipFile.close(zfile)
    print(i + 'successfully extracted to directory')

    # Clean up the Zip file created during the download process
    os.remove(os.path.join(shppath,i+".zip"))
    print(i + 'Successfully deleted zip')

    # Use ArcPy Function to convert downloaded shapes to FC's in the GDB
    arcpy.FeatureClassToFeatureClass_conversion(os.path.join(shppath,i+".shp"),
            gdbpath,gdbprefix+str.lower(i))
    print(i + 'Successfully merged into GeoDB')

    # Use ArcPy here Delete the Shapefiles downloaded. 
    arcpy.Delete_management(os.path.join(shppath,i+".shp"))
    print(i + 'Successfully Deleted shape ')

# Main Program Execution Area
def main():
    try:
        main_process()
        # shapefile_maker()
        print('Main Execution is complete')
    except:
        print('Main Failed.....back to the drawing board')
        print(arcpy.GetMessages())
        pass

main()