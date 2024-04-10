# Author :          Matt Herring
# Created Date :    May 08 , 2023
# Process Name :    nightly_min_aor_sj_sections
# Purporse :        joins aor polygons to the landgrid for improved reporting
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
sde = r"\\conoco.net\ho_shared\L48 GIS Secure\Land\mherring\connections\osde48p3.sde"
shape_folder = r'\\conoco.net\ho_shared\L48 GIS Secure\Land\mherring\automation\data\shps'
fc_sde_aor = r'\\conoco.net\ho_shared\L48 GIS Secure\Land\mherring\connections\osde48p3.sde\L48.LAND_AOR'
fc_sde_tx_sections = r'\\conoco.net\ho_shared\L48 GIS Secure\Land\mherring\connections\osde48p3.sde\TOBIN.TX_Sections'
fc_sde_l48_sections = r'\\conoco.net\ho_shared\L48 GIS Secure\Land\mherring\connections\osde48p3.sde\TOBIN.TWP_SECTIONS_TOBIN'
fc_out_sections_w_aor = r'\\conoco.net\ho_shared\L48 GIS Secure\Land\mherring\automation\pro\automation\automation.gdb\sects_w_aor'
bakken_aor_layer = r'\\conoco.net\ho_shared\L48 GIS Secure\Land\mherring\automation\python\aor\aor_sj_sections\layers\bakken_aor.lyrx'
output_geodb = r'\\conoco.net\ho_shared\L48 GIS Secure\Land\mherring\automation\pro\automation\automation.gdb'
nd_sections = arcpy.MakeFeatureLayer_management(fc_sde_l48_sections,"nd_sections_lyr","STATE = 33")
fc_l48_counties = r"\TOBIN.COUNTIES_TOBIN"
list_of_sde_fcs = ['L48.LAND_AOR','TOBIN.TWP_SECTIONS_TOBIN','TOBIN.COUNTIES_TOBIN']
list_of_local_fcs = ['COUNTIES_TOBIN','LAND_AOR','TWP_SECTIONS_TOBIN']
list_of_aut_fcs = ["aut_nd_results","aut_l48_counties" ]
qry_sections = """(SNAME = 'NORTH DAKOTA') And CNAME IN ('ADAMS', 'DUNN', 'HETTINGER','STARK','MCKENZIE')"""
qry_counties = """()"""
qry_state = """ (SNAME NOT IN ('NORTH DAKOTA', 'MONTANA', 'TEXAS')) """

# Delete FC's in the Output GeoDB. 
def delete_local_fcs():
    for fc in list_of_local_fcs:
        try:
            local_fc = os.path.join(output_geodb, fc)
            arcpy.Delete_management(local_fc)
            print(fc, "  - was successfully deleted. ")
            print(arcpy.GetMessages())
        except:
            print(fc, "either DNE or delete local fc's failed")
            return

# Delete Aut_FC's in the Output GeoDB. 
def delete_aut_fcs():
    for fc in list_of_aut_fcs:
        try:
            local_fc = os.path.join(output_geodb, fc)
            arcpy.Delete_management(local_fc)
            print(fc, "  - was successfully deleted. ")
            print(arcpy.GetMessages())
        except:
            print(fc, "either DNE or delete local fc's failed")
            return
        

# Copy SDE Data to Local GeoDB for analysis. 
def sde_fc_copy():
    try:        
        for fc in list_of_sde_fcs:
            fc_sde_loc = os.path.join(sde, fc)
            fc_local_path = os.path.join(output_geodb, fc)
            arcpy.Copy_management(fc_sde_loc, fc_local_path)
            print(fc, ' - has been copied. ')
            print(arcpy.GetMessages())
    except:
        print("sde_fc_copy failed.")

# make feature layer : sections in North Dakota (STATE = 33)
def sj_sections_to_aor():
    try:
        print("Beginning ND Analysis")
        in_features = os.path.join(output_geodb, list_of_local_fcs[2]) #2 is twp_sections_tobin
        join_features = os.path.join(output_geodb, list_of_local_fcs[1]) # 1 is Land AOR
        aor_fl = arcpy.MakeFeatureLayer_management(join_features,"bakken_aor","MANAGER = 'BRENDEN C KEYES'")
        out_fc = os.path.join(output_geodb, "aut_nd_results")
        nd_sections =   arcpy.MakeFeatureLayer_management(in_features,"nd_sections","STATE = 33") 
        arcpy.SpatialJoin_analysis(nd_sections,aor_fl,out_fc,"JOIN_ONE_TO_MANY","KEEP_COMMON","","INTERSECT","","" )
        print("ND Analysis Complete.")
        print(arcpy.GetMessages())
    except:
        print("Well that didn't work as planned. sj_sections_to_aor")

    
# create output datset for l48 aor by county. 
def sj_counties_to_aor():
    try:
        print("beginning aor by county analysis")
        local_counties = os.path.join(output_geodb, list_of_local_fcs[0]) # L48 Counties
        join_features = os.path.join(output_geodb, list_of_local_fcs[1]) # 1 is Land AOR
        aor_fl = arcpy.MakeFeatureLayer_management(join_features,"bakken_aor","MANAGER = 'BRENDEN C KEYES'")
        out_fc = os.path.join(output_geodb, "aut_l48_counties")
        arcpy.SpatialJoin_analysis(local_counties, aor_fl,out_fc,"JOIN_ONE_TO_MANY","KEEP_COMMON","","INTERSECT","","" )
    except:
        print("aor by county failed")
#############################################################
# To get this far, it is taking about 38 minutes in testing.# 
#############################################################

# Need to export the fc's to shapefiles. 
def create_shapefiles():
    try:
        for fc in list_of_aut_fcs:
            inputs = os.path.join(output_geodb, fc)
            output_folder = r"\\conoco.net\ho_shared\LANDINFO\RBU\1General & Admin\AOR Data\shapes"
            arcpy.FeatureClassToShapefile_conversion(inputs, output_folder)
            print(fc, ' - shapefile created successfully. ')
    except:
        print('shapefile generation failed. ')

# Create a couple Excel Datasheets for import into PowerBI
def create_excel_docs():
    try:
        for fc in list_of_aut_fcs:
            input = os.path.join(output_geodb, fc)
            print('beginning processing of' , fc)
            excel_folder = r"\\conoco.net\ho_shared\LANDINFO\RBU\1General & Admin\AOR Data\excel_from_gis"
            output = os.path.join(excel_folder, fc + '.xlsx')
        arcpy.TableToExcel_conversion(input, output)
        print('Data Table for ', fc ,  ' created successfully. ') 
    except: 
        print('Data Table Creation failed for' , fc)

# 
#   
# Main Program Execution Area
def main():
    try:
        start = time.time()
        delete_local_fcs()
        delete_aut_fcs()
        sde_fc_copy()
        sj_sections_to_aor()
        sj_counties_to_aor()
        print('Main Execution is complete')
        print(arcpy.GetMessages())
        end = time.time()
        # print('The time of execution for main : ',  ((end-start) * 10**3) / 1000 ,"seconds")
        print('Main execution time : ',  ((((end-start) * 10**3) / 1000)/60) ,"Minutes")
    except:
        start = time.time()
        print('Main Failed.....back to the drawing board')
        print(arcpy.GetMessages())
        end = time.time()
        # print('Main Failed but it took  : ',  ((end-start) * 10**3) / 1000 ,"seconds")
        print('Main execution failed but it took : ',  ((((end-start) * 10**3) / 1000)/60) ,"Minutes")
        pass

# main()