import os

def delete_docx_with_pdf(folder_path):
    for root, dirs, files in os.walk(folder_path):
        pdf_present = any(file.endswith('.pdf') for file in files)
        if pdf_present:
            for file in files:
                if file.endswith('.docx'):
                    os.remove(os.path.join(root, file))

# Get the current directory where the script exists
current_directory = os.path.dirname(os.path.abspath(__file__))

# Call the function to delete docx files if PDFs are present
delete_docx_with_pdf(current_directory)

print("Docx files deleted successfully from folders containing at least one PDF file!")
