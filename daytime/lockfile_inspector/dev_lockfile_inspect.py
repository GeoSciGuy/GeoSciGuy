### Ai Generated. Bing Chat ***
import arcpy
import os
import win32security
import win32api

# variables
geodatabase_path = r'\\conoco.net\ho_shared\Maxwell_L48_RBU\MAX_General\Rockies\Bakken\Geo\@\ArcGIS\Bakken_Activity_Map\Geodatabase\Bakken Shapefiles\Facilities'
text_file_output_path = r'\\conoco.net\ho_shared\L48 GIS Secure\Land\mherring\data\bakken_data_in_sde\lock_analysis'


def get_lock_file_owners(geodatabase_path, text_file_output_path):
    lock_files = []
    for dirpath, dirnames, filenames in arcpy.da.Walk(geodatabase_path, datatype="Any", type="Lockfile"):
        for filename in filenames:
            lock_file_path = os.path.join(dirpath, filename)
            lock_files.append(lock_file_path)

    lock_file_owners = {}
    for lock_file in lock_files:
        lock_file_time = os.path.getmtime(lock_file)
        security_descriptor = win32security.GetFileSecurity(lock_file, win32security.OWNER_SECURITY_INFORMATION)
        owner_sid = security_descriptor.GetSecurityDescriptorOwner()
        owner_name, domain, type = win32security.LookupAccountSid(None, owner_sid)
        current_user_name = win32api.GetUserName()
        if owner_name == current_user_name:
            lock_file_owners[lock_file] = owner_name

    with open(text_file_output_path, "w") as text_file:
        for lock_file, owner_name in lock_file_owners.items():
            text_file.write(f"{lock_file}: {owner_name}\n")

    return lock_file_owners