import os
import shutil

# Define image file extensions to look for
IMAGE_EXTENSIONS = {'.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp'}

def contains_image(folder_path):
    """Check if the folder contains at least one image file."""
    for filename in os.listdir(folder_path):
        if any(filename.lower().endswith(ext) for ext in IMAGE_EXTENSIONS):
            return True
    return False

def move_to_complete(folder_path, complete_folder):
    """Move the folder to 'complete'."""
    try:
        shutil.move(folder_path, complete_folder)
        print(f"Moved {folder_path} to {complete_folder}")
    except Exception as e:
        print(f"Failed to move {folder_path}: {e}")

def main():
    # Get the current directory (where the script is located)
    current_dir = os.getcwd()
    
    # Create the 'complete' directory if it doesn't exist
    complete_folder = os.path.join(current_dir, 'complete')
    if not os.path.exists(complete_folder):
        os.makedirs(complete_folder)

    # Iterate through all subfolders in the current directory
    for root, dirs, files in os.walk(current_dir):
        # Skip the 'complete' folder itself to prevent recursion
        if os.path.abspath(root) == os.path.abspath(complete_folder):
            continue

        for folder in dirs:
            folder_path = os.path.join(root, folder)

            # Check if the folder contains an image
            if contains_image(folder_path):
                move_to_complete(folder_path, complete_folder)
            else:
                print(f"Folder {folder_path} is incomplete and remains unchanged.")

if __name__ == "__main__":
    main()
