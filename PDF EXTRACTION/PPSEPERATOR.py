import os
import shutil

# Get the directory where the script is located
source_directory = os.path.dirname(os.path.abspath(__file__))

# Define the directories for PP and non-PP files
pp_directory = os.path.join(source_directory, 'pp_files')
non_pp_directory = os.path.join(source_directory, 'non_pp_files')

# Create directories for PP and non-PP files if they don't exist
os.makedirs(pp_directory, exist_ok=True)
os.makedirs(non_pp_directory, exist_ok=True)

# List all files in the source directory
for filename in os.listdir(source_directory):
    # Get the full path of the file
    file_path = os.path.join(source_directory, filename)

    # Check if it's a file (not a directory) and if it has a .pdf extension
    if os.path.isfile(file_path) and filename.endswith('.pdf') and filename != os.path.basename(__file__):
        # Check if the filename (excluding the extension) ends with ' PP'
        if filename[:-4].endswith(' PP'):
            # Move the file to the PP directory
            shutil.move(file_path, os.path.join(pp_directory, filename))
        else:
            # Move the file to the non-PP directory
            shutil.move(file_path, os.path.join(non_pp_directory, filename))

print("PDF files have been separated into PP and non-PP directories.")
