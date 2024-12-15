import os
import shutil
import tkinter as tk
from tkinter import messagebox

# Get the current directory of the script
script_dir = os.path.dirname(os.path.realpath(__file__))

# Create a separate folder named 'only pdfs' if it doesn't exist
pdf_folder = os.path.join(script_dir, 'only pdfs')
if not os.path.exists(pdf_folder):
    os.makedirs(pdf_folder)

# Create subfolders for PP and non-PP files
pp_folder = os.path.join(pdf_folder, 'pp_files')
non_pp_folder = os.path.join(pdf_folder, 'non_pp_files')
os.makedirs(pp_folder, exist_ok=True)
os.makedirs(non_pp_folder, exist_ok=True)

# Initialize counters for PP and non-PP files
pp_count = 0
non_pp_count = 0

# Define a function to copy PDF files recursively, ignoring the 'only pdfs' folder and current directory
def copy_pdfs(src_dir):
    global pp_count, non_pp_count
    for root, dirs, files in os.walk(src_dir):
        # Skip the current directory and the 'only pdfs' folder
        if root == src_dir:
            # Remove 'only pdfs' folder from the list of directories to traverse
            dirs[:] = [d for d in dirs if d != 'only pdfs']
            continue
        for file in files:
            if file.lower().endswith('.pdf'):
                src_file = os.path.join(root, file)
                # Check if the filename (excluding the extension) ends with ' PP'
                if file[:-4].endswith(' PP'):
                    dest_folder = pp_folder
                    pp_count += 1
                else:
                    dest_folder = non_pp_folder
                    non_pp_count += 1
                dest_file = os.path.join(dest_folder, file)
                shutil.copy(src_file, dest_file)
                print(f"Copied: {src_file} to {dest_file}")

# Call the function with the current directory
copy_pdfs(script_dir)

# Display the counts in a GUI
root = tk.Tk()
root.withdraw()  # Hide the root window

message = f"PDF files have been separated into PP and non-PP folders within 'only pdfs'.\n\nPP files: {pp_count}\nNon-PP files: {non_pp_count}"
messagebox.showinfo("File Separation Complete", message)

print(message)
