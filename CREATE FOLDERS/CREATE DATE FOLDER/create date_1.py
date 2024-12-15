import os
from datetime import datetime
import shutil
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import DateEntry

def create_folders_and_copy_files(custom_date):
    # Define the folder name using the custom date
    folder_name = f"{custom_date.strftime('%d.%m.%Y')} COMPLETE DOCUMENTS"

    # Get the current working directory
    current_directory = os.getcwd()

    # Create the new folder in the current directory
    new_folder_path = os.path.join(current_directory, folder_name)
    os.makedirs(new_folder_path, exist_ok=True)

    # Define the list of subfolder names inside COMPLETE DOCUMENTS
    subfolders = ["incomplete","Images"]  # Edit this list to add/remove subfolders

    # Create the subfolders inside the "COMPLETE DOCUMENTS" folder
    for subfolder_name in subfolders:
        subfolder_path = os.path.join(new_folder_path, subfolder_name)
        os.makedirs(subfolder_path, exist_ok=True)

        print(f"Subfolder '{subfolder_name}' created inside '{folder_name}'.")

    # Define the list of files to be copied into the folder
    files_to_copy = ['changeimageinpp.py','PP.docx','PP.pdf','simplepeople folder.py' ,'for_people_folder.py', 'pdffolder check.py', 'pdfallmergeall.py']  # Add more file names as needed

    for file_name in files_to_copy:
        # Define the destination path for the copied files
        destination_path = os.path.join(new_folder_path, file_name)

        # Copy the files to the "COMPLETE DOCUMENTS" folder
        if os.path.exists(file_name):
            shutil.copy(file_name, destination_path)
            print(f"File '{file_name}' copied to '{folder_name}' folder.")
        else:
            print(f"File '{file_name}' does not exist. Skipping.")

def get_date_and_execute():
    selected_date = cal.get_date()
    root.destroy()  # Close the GUI window
    create_folders_and_copy_files(selected_date)

def enter_pressed(event):
    get_date_and_execute()

# Create the main application window
root = tk.Tk()
root.title("Select Date")

# Make the window the active window as soon as it launches
root.focus_force()

# Create a frame for better layout management
frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Add a label to the frame
ttk.Label(frame, text="Please select a date:").grid(column=1, row=1, padx=10, pady=10)

# Add the DateEntry widget to the frame with DD/MM/YYYY format
cal = DateEntry(frame, width=12, background='darkblue', foreground='white', borderwidth=2, date_pattern='dd/MM/yyyy')
cal.grid(column=2, row=1, padx=10, pady=10)

# Add a button to the frame to get the selected date
select_button = ttk.Button(frame, text="Select", command=get_date_and_execute)
select_button.grid(column=1, row=2, columnspan=2, pady=10)

# Bind the Enter key to simulate the "Select" button click
root.bind('<Return>', enter_pressed)

# Run the application
root.mainloop()
