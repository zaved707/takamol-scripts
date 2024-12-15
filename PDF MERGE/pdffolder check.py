import os
import tkinter as tk
from tkinter import messagebox
import re

def check_pdfs_in_subfolders():
    # Get the current directory
    current_directory = os.getcwd()
    
    # Loop through all subfolders
    invalid_folders = []
    for folder in os.listdir(current_directory):
        folder_path = os.path.join(current_directory, folder)
        
        if os.path.isdir(folder_path):
            # Get all PDF files in the subfolder
            pdf_files = [f for f in os.listdir(folder_path) if f.lower().endswith('.pdf')]
            
            # If the folder is empty, add it to the invalid folders
            if len(pdf_files) == 0:
                invalid_folders.append([folder])  # Add folder name as invalid
                continue  # Skip further checks for this folder
            
            # Check if there are exactly two PDFs
            if len(pdf_files) == 2:
                # Separate based on the 'PP' suffix
                pp_files = [f for f in pdf_files if f.lower().endswith('pp.pdf')]
                non_pp_files = [f for f in pdf_files if not f.lower().endswith('pp.pdf')]
                
                # Check if one file has 'PP' and the other does not
                if len(pp_files) != 1 or len(non_pp_files) != 1:
                    invalid_folders.append(pdf_files)
            else:
                # If the folder has more or less than 2 PDF files
                invalid_folders.append(pdf_files)
    
    return invalid_folders

def display_result(invalid_folders):
    # Create the tkinter window
    root = tk.Tk()
    root.withdraw()  # Hide the main window (we just need the message box)
    
    if invalid_folders:
        # Show the invalid folders and files
        message = "The following subfolders do not meet the requirements:\n"
        for files in invalid_folders:
            message += f"{', '.join(files)}\n"
        messagebox.showerror("Invalid Folders", message)
    else:
        # Show "Yes" if everything is correct
        messagebox.showinfo("Success", "Yes, all subfolders meet the criteria!")

    root.quit()

def main():
    # Check the PDFs in subfolders
    invalid_folders = check_pdfs_in_subfolders()
    
    # Display the result in a GUI
    display_result(invalid_folders)

if __name__ == "__main__":
    main()
