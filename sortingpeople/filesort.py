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

def move_incomplete_folder(folder_path, incomplete_folder):
    """Move the folder to 'incomplete'."""
    try:
        shutil.move(folder_path, incomplete_folder)
        print(f"Moved {folder_path} to {incomplete_folder}")
    except Exception as e:
        print(f"Failed to move {folder_path}: {e}")

def main():
    # Get the current directory (where the script is located)
    current_dir = os.getcwd()
    
    # Create the 'incomplete' directory if it doesn't exist
    incomplete_folder = os.path.join(current_dir, 'incomplete')
    if not os.path.exists(incomplete_folder):
        os.makedirs(incomplete_folder)

    # Iterate through all subfolders in the current directory
    for root, dirs, files in os.walk(current_dir):
        # Skip the 'incomplete' folder itself to prevent recursion
        if os.path.abspath(root) == os.path.abspath(incomplete_folder):
            continue

        for folder in dirs:
            folder_path = os.path.join(root, folder)

            # Check if the folder contains an image
            if not contains_image(folder_path):
                move_incomplete_folder(folder_path, incomplete_folder)

if __name__ == "__main__":
    main()
