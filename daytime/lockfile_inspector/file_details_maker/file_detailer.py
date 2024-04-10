import os

def get_file_info(root_path):
    for root, dirs, files in os.walk(root_path):
        for file in files:
            file_path = os.path.join(root, file)
            file_name = os.path.basename(file_path)
            print(f"File Name: {file_name}\nFile Path: {file_path}\n")
        for dir in dirs:
            dir_path = os.path.join(root, dir)
            dir_name = os.path.basename(dir_path)
            print(f"Directory Name: {dir_name}\nDirectory Path: {dir_path}\n")
