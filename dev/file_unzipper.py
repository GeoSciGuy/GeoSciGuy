import os
import zipfile

input_folder = input("Enter the path of the input folder: ")
output_folder = input("Enter the path of the output folder: ")

for file in os.listdir(input_folder):
    if file.endswith(".zip"):
        with zipfile.ZipFile(os.path.join(input_folder, file), "r") as zip_ref:
            zip_ref.extractall(output_folder)
            print(file + "has been unzipped.")