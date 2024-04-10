import ftplib
import os
import zipfile

filename = input("Enter the filename: ")
source_url = input("Enter the source URL: ")
username = input("Enter the username: ")
password = input("Enter the password: ")
local_zip_path = input("Enter the local zip path: ")
unzipped_path = input("Enter the unzipped path: ")

ftp = ftplib.FTP(source_url)
ftp.login(username, password)

with open(local_zip_path, "wb") as f:
    ftp.retrbinary("RETR " + filename, f.write)

ftp.quit()

with zipfile.ZipFile(local_zip_path, "r") as zip_ref:
    zip_ref.extractall(unzipped_path)

os.remove(local_zip_path)