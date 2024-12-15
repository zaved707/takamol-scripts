import os
import shutil

# Get the current directory of the script
script_dir = os.path.dirname(os.path.realpath(__file__))

# Create a separate folder named 'only pdfs' if it doesn't exist
pdf_folder = os.path.join(script_dir, 'only docx')
if not os.path.exists(pdf_folder):
    os.makedirs(pdf_folder)

# Define a function to copy PDF files recursively, ignoring the 'only pdfs' folder
def copy_pdfs(src_dir):
    for root, dirs, files in os.walk(src_dir):
        if 'only docx' in dirs:
            dirs.remove('only docx')  # Ignore 'only pdfs' folder
        for file in files:
            if file.lower().endswith('.docx'):
                src_file = os.path.join(root, file)
                dest_file = os.path.join(pdf_folder, file)
                shutil.copy(src_file, dest_file)
                print(f"Copied: {src_file} to {dest_file}")

# Call the function with the current directory
copy_pdfs(script_dir)
