import os
from datetime import datetime
import shutil

# Get custom date input from the user
custom_date_str = input("Enter the date in format DD.MM.YYYY: ")

try:
    custom_date = datetime.strptime(custom_date_str, "%d.%m.%Y")
except ValueError:
    print("Invalid date format. Please enter the date in DD.MM.YYYY format.")
    exit()

# Define the folder names using the custom date
folder_name = f"{custom_date.strftime('%d.%m.%Y')} COMPLETE DOCUMENTS"
first_half_folder = f"{custom_date.strftime('%d.%m.%Y')} FIRST HALF"
second_half_folder = f"{custom_date.strftime('%d.%m.%Y')} SECOND HALF"

# Get the current working directory
current_directory = os.getcwd()

# Create the new folders in the current directory
new_folder_path = os.path.join(current_directory, folder_name)
os.makedirs(new_folder_path, exist_ok=True)

# Create "FIRST HALF" and "SECOND HALF" folders inside "COMPLETE DOCUMENTS"
first_half_path = os.path.join(new_folder_path, first_half_folder)
os.makedirs(first_half_path, exist_ok=True)

second_half_path = os.path.join(new_folder_path, second_half_folder)
os.makedirs(second_half_path, exist_ok=True)

subfolders = ["pending", "incomplete practical", "incomplete theory"]

# Iterate through the list of subfolder names and create each subfolder inside both halves
for subfolder_name in subfolders:
    first_half_subfolder_path = os.path.join(first_half_path, subfolder_name)
    os.makedirs(first_half_subfolder_path, exist_ok=True)
    
    second_half_subfolder_path = os.path.join(second_half_path, subfolder_name)
    os.makedirs(second_half_subfolder_path, exist_ok=True)

    print(f"Subfolders '{subfolder_name}' created inside '{first_half_folder}' and '{second_half_folder}'.")

# Define the list of files to be copied into each half folder
files_to_copy = ['PP.docx', 'for_people_folder.py', 'PDF EXTRACTION.py']  # Add more file names as needed

for file_name in files_to_copy:
    # Define the destination paths for the copied files in both halves
    first_half_destination_path = os.path.join(first_half_path, file_name)
    second_half_destination_path = os.path.join(second_half_path, file_name)
    
    # Copy the files to both halves
    shutil.copy(file_name, first_half_destination_path)
    shutil.copy(file_name, second_half_destination_path)
    
    print(f"File '{file_name}' copied to '{first_half_folder}' and '{second_half_folder}' folders.")
