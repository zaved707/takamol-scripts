import os
#this program deletes all python files from the folder its in and all its subfolders. except itself
def delete_python_files(folder_path):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.py') and file != os.path.basename(__file__):  # Exclude the script file itself
                os.remove(os.path.join(root, file))

# Get the current directory where the script exists
current_directory = os.path.dirname(os.path.abspath(__file__))

# Call the function to delete Python files
delete_python_files(current_directory)

print("Python files deleted successfully!")
