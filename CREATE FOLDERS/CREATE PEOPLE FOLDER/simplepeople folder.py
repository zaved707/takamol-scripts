import os
import shutil

# Prompt for the name
name = input("Enter your name: ")

# Define the new folder path using the name
new_folder_path = os.path.join(os.getcwd(), name)

# Check if the folder already exists, if not, create it
if not os.path.exists(new_folder_path):
    os.makedirs(new_folder_path)
    print(f"Folder '{name}' created successfully.")
else:
    print(f"Folder '{name}' already exists.")

# Define the source file (PP.docx in the script's directory)
source_file = os.path.join(os.getcwd(), 'PP.docx')

# Check if the file exists
if os.path.exists(source_file):
    # Define the destination file name with the name prefix
    destination_file_name = f"{name} PP.docx"
    destination_file = os.path.join(new_folder_path, destination_file_name)
    
    # Copy the file to the new folder with the new name
    shutil.copy(source_file, destination_file)
    print(f"File 'PP.docx' copied to '{destination_file}'.")
else:
    print("Error: 'PP.docx' file not found in the script's directory.")
