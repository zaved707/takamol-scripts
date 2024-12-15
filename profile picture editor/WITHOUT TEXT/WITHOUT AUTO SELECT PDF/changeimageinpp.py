import fitz  # PyMuPDF
from tkinter import Tk, filedialog, messagebox
import os
import re

def select_file(title, filetypes, initialdir):
    root = Tk()
    root.withdraw()  # Hide the main window
    selected_file = filedialog.askopenfilename(title=title, filetypes=filetypes, initialdir=initialdir)
    root.destroy()  # Destroy the root window after selection
    return selected_file

def show_error_and_select_file(message, title, filetypes, initialdir):
    while True:
        root = Tk()
        root.withdraw()  # Hide the main window
        messagebox.showerror("Error", message)  # Show error message
        root.focus_force()  # Bring the focus to the error message box
        root.destroy()  # Destroy the root window after showing the error
        
        selected_file = select_file(title, filetypes, initialdir)
        if selected_file.lower().endswith('.pdf'):
            return selected_file

# Function to find the target file automatically
def find_target_file(directory):
    for file in os.listdir(directory):
        if re.match(r'^[A-Z0-9\s]+ PP\.\w{3,4}$', file, re.IGNORECASE):
            return os.path.join(directory, file)
    return None

# Get the current working directory
current_directory = os.getcwd()

# Find the target PDF file automatically
#pdf_file = find_target_file(current_directory)
'''if not pdf_file:
    print("No target PDF file found. Please select a PDF file manually.")'''
pdf_file = select_file("Select PDF File", (("PDF files", "*.pdf"), ("All files", "*.*")), current_directory)
if not pdf_file:
    print("No PDF file selected.")
    exit()


# Check if the selected file is a PDF (case-insensitive)
if not pdf_file.lower().endswith('.pdf'):
    pdf_file = show_error_and_select_file("The selected file is not a PDF. Please select a valid PDF file.", 
                                          "Select PDF File", (("PDF files", "*.pdf"), ("All files", "*.*")), current_directory)
    if not pdf_file:
        print("No PDF file selected.")
        exit()

# Open the selected PDF document
doc = fitz.open(pdf_file)

# Insert text into the first page
page_number = 0  # Page numbers are zero-indexed
page = doc[page_number]

'''
# Define the start point of the first line of text
p = fitz.Point(555, 53)  # bottom-left of the first character

# Prompt user to enter a number between 0 and 10
while True:
    user_input = input("Please enter THE TASK NUMBER: ")
    if user_input.isdigit():
        # Convert to integer and format it as '00'
        number = int(user_input)
        formatted_number = f"{number:02}"  # Format as two digits
        break
    else:
        print("Invalid input. Please enter a valid number.")


# Insert the formatted number into the page
rc = page.insert_text(p,  # bottom-left of 1st char
                     formatted_number,  # the text (honors '\n')
                     fontname = "helv",  # the default font
                     fontsize = 11,  # the default font size
                     rotate = 0,  # also available: 90, 180, 270
                     )

print("%i lines printed on page %i." % (rc, page.number + 1))  # page.number is zero-indexed
'''
# Prompt the user to select an image for each page
# Prompt the user to select an image for each page
for page_index in range(len(doc)):  # Iterate over PDF pages
    page = doc[page_index]  # Get the page
    
    page_width = page.rect.width
    page_height = page.rect.height
    
    # Prompt the user to select an image
    image_file = select_file("Select Image File", (("Image files", "*.png;*.jpg;*.jpeg;*.gif;*.bmp;*.tiff"), ("All files", "*.*")), current_directory)
    if not image_file:  # If the user cancels image selection
        print("No image file selected.")
        break
    
    image = fitz.open(image_file)
    
    # Get original image dimensions
    original_image_width = image[0].rect.width
    original_image_height = image[0].rect.height

    # Set the desired size for the image rectangle
    if page_index == 0:  # Special case for the first image
        target_width = 400
        target_height = 500  # Scale slightly smaller for the first page
    else:
        target_width = 400
        target_height = 600

    # Calculate the scaling factor for width and height
    width_ratio = target_width / original_image_width
    height_ratio = target_height / original_image_height

    # Use the smaller scaling factor to preserve aspect ratio
    scaling_factor = min(width_ratio, height_ratio)

    # Calculate the new width and height based on the scaling factor
    new_width = int(original_image_width * scaling_factor)
    new_height = int(original_image_height * scaling_factor)

    # Adjust the position for the first page image to be lower
    if page_index == 0:
        center_x = (page_width - new_width) / 2
        center_y = (page_height - new_height) / 2 + 60  # Push image lower by 100 units
    else:
        # Default centering for other pages
        center_x = (page_width - new_width) / 2
        center_y = (page_height - new_height) / 2

    # Insert the resized image at the calculated position
    page.insert_image(fitz.Rect(center_x, center_y, center_x + new_width, center_y + new_height), filename=image_file)


# Save the modified document with a temporary name
temp_output_file = pdf_file.replace(".pdf", "_temp.pdf")
doc.save(temp_output_file)

# Close the document to release the file
doc.close()

# Delete the original file
os.remove(pdf_file)

# Rename the temporary file to the original file name
os.rename(temp_output_file, pdf_file)

print(f"Modified PDF saved successfully as {pdf_file}")
