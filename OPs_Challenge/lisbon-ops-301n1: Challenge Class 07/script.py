#!/bin/python
import os
import subprocess

# Define a function to create a test directory with sub-directories
def create_test_directory(path):
    os.makedirs(path, exist_ok=True)
    print(f"Test directory '{path}' created successfully.")

    subdirs = [f"{path}_01", f"{path}_02", f"{path}_03"]
    for subdir in subdirs:
        os.makedirs(f"{path}/{subdir}", exist_ok=True)
        print(f"Sub-directory '{subdir}' created successfully.")

def generate_file_list(path):
    file_list = []

    for root, dirs, files in os.walk(path):
        file_list.append(root)
    
        for file in files:
            file_list.append(os.path.join(root, file))

    return file_list



dirname = input("Enter the name for the test directory: ")
create_test_directory(dirname)
file_list = generate_file_list(dirname)

# Save the list to a text file
output_file = open("file_list.txt", "w")
for item in file_list:
    output_file.write(item + "\n")
output_file.close()

# Open LibreOffice
subprocess.run(["libreoffice", "--writer", "file_list.txt"])
print("File list saved to file_list.txt and opened with LibreOffice Writer.")

