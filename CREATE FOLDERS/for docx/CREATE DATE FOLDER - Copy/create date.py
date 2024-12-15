import os
from datetime import datetime
import shutil
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import DateEntry

def create_folders_and_copy_files(custom_date):
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
