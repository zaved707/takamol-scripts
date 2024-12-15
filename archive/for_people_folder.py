import os
import shutil

# Get the current working directory
current_directory = os.getcwd()

name = input('entre name \n')

# Define the new folder name
new_folder_name = name

# Create the new folder in the current directory
new_folder_path = os.path.join(current_directory, new_folder_name)
os.makedirs(new_folder_path, exist_ok=True)

print(f"Folder '{new_folder_name}' created in '{current_directory}'")

# Define the file to be copied
file_to_copy = 'PROFILE PICTURE.docx'  # Change 'example.txt' to the actual file name you want to copy

# Check if the file exists in the current directory
if os.path.isfile(file_to_copy):
    # Prompt the user for input
    user_input = name
    
    # Construct the new file name with the user input as a prefix
    new_file_name = f"{user_input} {file_to_copy}"
    
    # Define the destination path for the copied file
    destination_path = os.path.join(new_folder_path, new_file_name)
    
    # Copy the file to the new folder with the new file name
    shutil.copy(file_to_copy, destination_path)
    
    print(f"File '{file_to_copy}' copied as '{new_file_name}' to '{new_folder_name}' folder.")
else:
    print(f"File '{file_to_copy}' not found in '{current_directory}'.")
