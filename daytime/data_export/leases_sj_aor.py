# This script will take the lease layer spatially joined to the aor and export it. 
# Using ArcPy to accomplish this. 

# Author :          Matt Herring
# Created Date :    |7-13-2023
# Process Name :    |leases_sj_aor.py
# Purporse :        |export attributes from gis layer to tabular form consumption
###############################################################################

# Setup Enviroment
# Import things
import arcpy
import os
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
shape_folder = r'\\conoco.net\ho_shared\L48 GIS Secure\Land\mherring\automation\data\shps'
geodb_path = r'\\conoco.net\ho_shared\L48 GIS Secure\Land\mherring\automation\pro\automation\automation.gdb'
lst_sde_data = ['RPA.NA_NONEXP_HDR_LSE', 'L48.LAND_AOR']


def leases_sj_aor():
    try:
        # arcpy.analysis.SpatialJoin(target_features, join_features, out_feature_class, {join_operation},
        #  {join_type}, {field_mapping}, {match_option}, {search_radius}, {distance_field_name})
        target_features = os.path.join(sde, r"RPA.NA_NONEXP_HDR_LSE")
        join_features = os.path.join(geodb_path, r"LAND_AOR" )
        out_feature_class = os.path.join(geodb_path, r"aut_L48_leases_sj_aor")
        # def_qry = r''' "ARRG_STAT_DESC = 'Active" '''
        # join_operation = r'JOIN_ONE_TO_MANY'
        # join_type = r'KEEP_COMMON'
        # match_option = r'INTERSECT'
        arcpy.analysis.SpatialJoin(target_features, join_features, out_feature_class, 'JOIN_ONE_TO_MANY', 'KEEP_COMMON', '' ,'INTERSECT', '' , '' )
    except:
        print("Poop")  

# Main Program Execution Area
def main():
    start = time.time()
    try:
        leases_sj_aor()
        print('Main Execution is complete')
        print(arcpy.GetMessages())
        
    except:
        print('Main Failed.....back to the drawing board')
        print(arcpy.GetMessages())
        pass
    end = time.time()
    print('Main execution time : ',  ((((end-start) * 10**3) / 1000)/60) ,"Minutes")
    print(os.getlogin() + '- Main Execution is complete')

# Calls the Main Program    
main()