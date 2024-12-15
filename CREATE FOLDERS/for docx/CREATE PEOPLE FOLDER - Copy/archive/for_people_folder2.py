import os
import shutil

# Get the current working directory
current_directory = os.getcwd()

name = input('Enter name: ')
passport_number = input('Enter passport number: ')
ticket_number = input('Enter ticket number: ')
trade = input('Enter trade: ')

# Define the new folder name as a combination of name and trade
new_folder_name = f"{name} {trade}"

# Create the new folder in the current directory
new_folder_path = os.path.join(current_directory, new_folder_name)
os.makedirs(new_folder_path, exist_ok=True)

print(f"Folder '{new_folder_name}' created in '{current_directory}'")

# Define the file to be copied
file_to_copy = 'PP.docx'  # Change 'PP.docx' to the actual file name you want to copy

# Check if the file exists in the current directory
if os.path.isfile(file_to_copy):
    # Construct the new file name with the combination of name and trade as prefix
    new_file_name = f"{name} {trade} {file_to_copy}"
    
    # Define the destination path for the copied file
    destination_path = os.path.join(new_folder_path, new_file_name)
    
    # Copy the file to the new folder with the new file name
    shutil.copy(file_to_copy, destination_path)
    
    print(f"File '{file_to_copy}' copied as '{new_file_name}' to '{new_folder_name}' folder.")

    # Create 'details.txt' file and write details to it
    details_file_path = os.path.join(new_folder_path, 'details.txt')
    with open(details_file_path, 'w') as details_file:
        details_file.write(f'name {name}\n')
        details_file.write(f'passport number {passport_number}\n')
        details_file.write(f'ticket number {ticket_number}\n')
        details_file.write(f'trade {trade}\n')

    print(f"'details.txt' file created with details in '{new_folder_name}' folder.")
else:
    print(f"File '{file_to_copy}' not found in '{current_directory}'.")
