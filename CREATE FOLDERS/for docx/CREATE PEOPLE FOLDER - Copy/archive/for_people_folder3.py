import os
import shutil
import tkinter as tk
from tkinter import ttk

# Define the trade options for the dropdown menu
trade_options = ['ELECTRICIAN', 'PLUMBING', 'TILING', 'WELDING', 'BLACKSMITH', 'CARPENTRY', 'HVAC', 'CAR BODY REPAIR',
                 'CONSTRUCTION AND BUILDING', 'PAINTING', 'PLASTERER', 'AUTOMOTIVE ELECTRICIAN', 'AUTOMOTIVE MECHANICS']

# Get the current working directory
current_directory = os.getcwd()

# Create a Tkinter window for data input
root = tk.Tk()
root.title("Enter Details")

# Create a frame to hold input fields
input_frame = ttk.Frame(root, padding=20)
input_frame.pack()

# Function to handle button click
def create_folder():
    # Get input values
    name = name_entry.get()
    passport_number = passport_entry.get()
    ticket_number = ticket_entry.get()
    selected_trade = trade_dropdown.get()

    # Define the new folder name as a combination of name and trade
    new_folder_name = f"{name} {selected_trade}"

    # Create the new folder in the current directory
    new_folder_path = os.path.join(current_directory, new_folder_name)
    os.makedirs(new_folder_path, exist_ok=True)

    print(f"Folder '{new_folder_name}' created in '{current_directory}'")

    # Define the file to be copied
    file_to_copy = 'PP.docx'  # Change 'PP.docx' to the actual file name you want to copy

    # Check if the file exists in the current directory
    if os.path.isfile(file_to_copy):
        # Construct the new file name with the combination of name and trade as prefix
        new_file_name = f"{name} {selected_trade} {file_to_copy}"

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
            details_file.write(f'trade {selected_trade}\n')

        print(f"'details.txt' file created with details in '{new_folder_name}' folder.")
    else:
        print(f"File '{file_to_copy}' not found in '{current_directory}'.")

    # Close the GUI window after folder creation
    root.destroy()

# Function to move focus to the next input field
def move_focus(event):
    event.widget.tk_focusNext().focus()

# Label and entry for Name
name_label = ttk.Label(input_frame, text="Enter Name:")
name_label.grid(row=0, column=0, padx=5, pady=5)
name_entry = ttk.Entry(input_frame)
name_entry.grid(row=0, column=1, padx=5, pady=5)
name_entry.bind('<Return>', move_focus)  # Move focus to the next field on Enter press

# Label and entry for Passport Number
passport_label = ttk.Label(input_frame, text="Enter Passport Number:")
passport_label.grid(row=1, column=0, padx=5, pady=5)
passport_entry = ttk.Entry(input_frame)
passport_entry.grid(row=1, column=1, padx=5, pady=5)
passport_entry.bind('<Return>', move_focus)  # Move focus to the next field on Enter press

# Label and entry for Ticket Number
ticket_label = ttk.Label(input_frame, text="Enter Ticket Number:")
ticket_label.grid(row=2, column=0, padx=5, pady=5)
ticket_entry = ttk.Entry(input_frame)
ticket_entry.grid(row=2, column=1, padx=5, pady=5)
ticket_entry.bind('<Return>', move_focus)  # Move focus to the next field on Enter press

# Label and dropdown for Trade
trade_label = ttk.Label(input_frame, text="Select Trade:")
trade_label.grid(row=3, column=0, padx=5, pady=5)
selected_trade = tk.StringVar()
trade_dropdown = ttk.Combobox(input_frame, textvariable=selected_trade, values=trade_options)
trade_dropdown.grid(row=3, column=1, padx=5, pady=5)
trade_dropdown.current(0)  # Set default value for the dropdown
trade_dropdown.bind('<Return>', lambda event: create_folder())  # Create folder on Enter press

# Button to create folder and copy file
create_button = ttk.Button(input_frame, text="Create Folder and Copy File", command=create_folder)
create_button.grid(row=4, column=0, columnspan=2, pady=10)

# Run the Tkinter main loop
root.mainloop()
