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

# Define the folder name using the custom date
folder_name = f"{custom_date.strftime('%d.%m.%Y')} COMPLETE DOCUMENTS"

# Get the current working directory
current_directory = os.getcwd()

# Create the new folder in the current directory
new_folder_path = os.path.join(current_directory, folder_name)
os.makedirs(new_folder_path, exist_ok=True)

subfolders = ["pending", "incomplete practical", "incomplete theory"]

# Iterate through the list of subfolder names and create each subfolder
for subfolder_name in subfolders:
    subfolder_path = os.path.join(new_folder_path, subfolder_name)
    os.makedirs(subfolder_path, exist_ok=True)
    print(f"Subfolder '{subfolder_name}' created inside '{folder_name}'")


print(f"Folder '{folder_name}' created in '{current_directory}'")

# Define the list of files to be copied
files_to_copy = ['PROFILE PICTURE.docx', 'for_people_folder.py']  # Add more file names as needed

for file_name in files_to_copy:
    # Check if the file exists in the current directory
    if os.path.isfile(file_name):
        # Define the destination path for the copied file
        destination_path = os.path.join(new_folder_path, file_name)
        
        # Copy the file to the new folder
        shutil.copy(file_name, destination_path)
        
        print(f"File '{file_name}' copied to '{folder_name}' folder.")
    else:
        print(f"File '{file_name}' not found in '{current_directory}'.")
