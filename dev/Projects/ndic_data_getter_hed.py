# Author :          Matt Herring                                                      #
# Created Date :    03-30-2022                                                        #
# Process Name :    ndic_data_getter                                                  #
# Purporse :        atuomatically download several shape files from the NDIC website  #
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
import time
# ## Third Party
# GIS Things
import arcpy
import logging


# Set Env Variables for ArcPy
arcpy.env.overwriteOutput = True
arcpy.env.qualifiedFieldNames = False
arcpy.env.parallelProcessingFactor = "96%"
# arcpy.env.workspace = r'\\conoco.net\ho_shared...'
# arcpy.env.scratchWorkspace = r'\\conoco.net\ho_shared'

# Set Variables for functions ( Global)
# datapath = r'\\conoco.net\ho_shared\RBU_GIS_SECURE\greater_williston\data'
datapath = r'\\conoco.net\ho_shared\GIS_Data\Users\M_HERRING\ndic'
# shppath = os.path.join(datapath,r'shp\ndic')
# gdbpath = os.path.join(datapath,r'gdb\rbu_gw_principal_fgdb.gdb')
shppath = os.path.join(datapath,r'shp')
gdbpath = os.path.join(datapath,r'published_ndic.gdb')


# url = "https://www.dmr.nd.gov/output/ShapeFiles/"
url = "https://gis.dmr.nd.gov/downloads/oilgas/shapefile/"
#lst = ['BLMLands','CasesDocketed','CityBoundaries','CountyRoads','Directionals','DrillingSpacingUnits','FederalForestService','FortBerthold_Surface','GasPlants','Horizontals_Lines','MajorRivers','MajorRoads','NDLandDept','OilFields','PermitStatusBeforeSpud','Reservations','UnitBoundaries','Wells']
#lst = ['MajorRoads','MissouriRiver','NDLandDept','OilFields','PermitStatusBeforeSpud','Reservations','Rigs','Sections','Seismic2DPreplot','Seismic3DPreplot','Townships','UnitBoundaries','Wells',]
#lst = ['BLMLands','CasesDocketed','CityBoundaries','CountyBoundaries','CountyRoads','Directionals','Directionals_Lines','DrillingSpacingUnits','FederalForestService','FedForestService','FortBerthold_Mineral','FortBerthold_Surface','GasPlants','Horizontals','Horizontals_Lines','InspectorAreas','MajorRivrs','MajorRoads','MissouriRiver','NDLandDept','OilFields','PermitStatusBeforeSpud','Reservations','Rigs','Sections','Seismic2DPreplot','Seismic3DPreplot','Townships','UnitBoundaries','Wells',]
lst = ['MissouriRiver','MajorRivers','OGD_CasesDocketed', 'OGD_Directionals', 'OGD_Directionals_Line', 'OGD_DrillingSpacingUnits', 'OGD_GasPlants','OGD_Horizontals','OGD_Horizontals_Line','OGD_InspectorAreas','OGD_OilFields','OGD_PermitStatusBeforeSpud','OGD_Rigs','OGD_Seismic2DPreplot','OGD_Seismic3DPreplot','OGD_UnitBoundaries','OGD_Wells']
gdbprefix = "L48_gcr_bakken_ndic_"

# Begin Code Section

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
        try:

            # create a variable zip, and use urllib to open the URL
            # logging.info('Beginning Processing for ' , i)
            # print('Beginning processing for ' , i)

            zip = urllib.request.urlopen(url+i+".zip",)
            # read the zip file after urllib has opened the link
            with open(os.path.join(shppath,i+".zip"),'wb') as output:
                # read the zip file into memory for additional processing
                output.write(zip.read())
                # Create a zipfile variable and assign it the currently handled 'i'
                print(i + ' successfully read from website, beginning zipfile creation')
                # logging.info(i , "successfully read from website , beginning zipefile creation")
                zfile = zipfile.ZipFile(os.path.join(shppath,i+".zip"),'r')
                # Extract the Current 'i' zipfile
                zfile.extractall(os.path.join(shppath))
    
                # Close the currently being read zip file, best practice here. 
                zipfile.ZipFile.close(zfile)
                print(i + ' successfully extracted to directory and zip gracefully closed, beginning fc creation')
                # logging.info(i , "successfully extracted to directory and zip gracefully closed, beginning fc creation")
                # Use ArcPy Function to convert downloaded shapes to FC's in the GDB
                arcpy.FeatureClassToFeatureClass_conversion(os.path.join(shppath, i+".shp"),
                        gdbpath,gdbprefix+str.lower(i))
                print(i + ' Successfully merged into GeoDB, now deleting the shapes')
                # logging.info(i + ' Successfully merged into GeoDB, now deleting the shapes')
                ## Use ArcPy here Delete the Shapefiles downloaded.
                arcpy.Delete_management(os.path.join(shppath, i + r'.shp'))
                print(i + " Shape was Successfully Deleted, moving on to the next NDIC Dataset")
                # logging.info(i + " Shape was Successfully Deleted, moving on to the next NDIC Dataset")
        except:
            print(i + "- Well that didn't work, look at work succeeded last")

# Iterate through and delete all zips
def zip_cleanup():
    for i in lst:
        try:
            ## Use os.remove to delete downloaded zip files
            # print(i + '.zip is about to be deleted')
            # logging.info(i + "zip is about to be deleted.")
            os.remove((os.path.join(shppath,i + r'.zip')))
            print ( i + "- zip has been deleted")
            # logging.info(i + "zip has been deleted. ")
        except:
            print (i + ' - zip deletion has failed')

# Main Program Execution Area
def main():
    start = time.time()
    #logging.basicConfig(filename='ndic_data_getter.log' , format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p' , level=logging.INFO)
    #logging.info('******   Is when the NDIC Data Getter process event Started      *********')
    try:
        main_process()
        zip_cleanup()
        print(os.getlogin() + '- Main Execution is complete')
    except:
        print('Main Failed.....back to the drawing board')
        print(arcpy.GetMessages())
        pass
    end = time.time()
    #logging.info('Finished Execution, All data downloaded. ')
    print('The time of execution for merging input data was : ',  ((end-start) * 10**3) / 1000 ,"seconds")
    print('Main execution time : ',  ((((end-start) * 10**3) / 1000)/60) ,"Minutes")

main()