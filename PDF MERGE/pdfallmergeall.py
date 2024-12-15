import os
import tkinter as tk
from tkinter import messagebox
import PyPDF2

def check_pdfs_in_subfolders():
    # Get the current directory
    current_directory = os.getcwd()
    
    # Loop through all subfolders
    invalid_folders = []
    valid_folders = []
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
                if len(pp_files) == 1 and len(non_pp_files) == 1:
                    valid_folders.append((folder_path, non_pp_files[0], pp_files[0]))
                else:
                    invalid_folders.append(pdf_files)
            else:
                # If the folder has more or less than 2 PDF files
                invalid_folders.append(pdf_files)
    
    return invalid_folders, valid_folders

def combine_pdfs(folder_path, non_pp_pdf, pp_pdf):
    # Combine the two PDFs with the non-PP file first
    non_pp_path = os.path.join(folder_path, non_pp_pdf)
    pp_path = os.path.join(folder_path, pp_pdf)
    
    # Create a PDF merger object
    pdf_merger = PyPDF2.PdfMerger()
    
    # Append PDFs in the correct order (non-PP first)
    pdf_merger.append(non_pp_path)
    pdf_merger.append(pp_path)
    
    # Output the combined PDF in the same folder, with the folder name at the front
    folder_name = os.path.basename(folder_path)  # Get the folder name
    output_pdf_path = os.path.join(folder_path, f'combined_{folder_name}.pdf')
    pdf_merger.write(output_pdf_path)
    pdf_merger.close()
    
def display_result(invalid_folders, valid_folders):
    # Create the tkinter window
    root = tk.Tk()
    root.withdraw()  # Hide the main window (we just need the message box)
    
    # Display invalid folders
    if invalid_folders:
        message = "The following subfolders do not meet the requirements:\n"
        for files in invalid_folders:
            message += f"{', '.join(files)}\n"
        messagebox.showerror("Invalid Folders", message)
    else:
        messagebox.showinfo("Success", "Yes, all subfolders meet the criteria!")
    
    # Display processing result
    if valid_folders:
        for folder_path, non_pp_pdf, pp_pdf in valid_folders:
            combine_pdfs(folder_path, non_pp_pdf, pp_pdf)
        messagebox.showinfo("Processing Completed", "PDFs were successfully combined in the valid folders.")
    
    # Show a final message after all operations are done
    messagebox.showinfo("All Operations Complete", "All PDF merging tasks have been completed.")

    root.quit()

def main():
    # Check the PDFs in subfolders
    invalid_folders, valid_folders = check_pdfs_in_subfolders()
    
    # Display the result in a GUI
    display_result(invalid_folders, valid_folders)

if __name__ == "__main__":
    main()
