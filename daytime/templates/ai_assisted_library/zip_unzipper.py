import os
import zipfile

input_folder = input("Enter the input folder location: ")
extension = ".zip"

for item in os.listdir(input_folder):
    if item.endswith(extension):
        file_path = os.path.join(input_folder, item)
        with zipfile.ZipFile(file_path, 'r') as zip_ref:
            zip_ref.extractall(input_folder)