import os
#THIS SCRIPT DELETES ALL THE IMAGES IF THE FOLDERS CONDTAIN VIDEO
# Get the current script's directory
script_directory = os.path.dirname(os.path.abspath(__file__))

# Get a list of all subfolders in the script's directory
subfolders = [f.path for f in os.scandir(script_directory) if f.is_dir()]

# Iterate through each subfolder
for subfolder in subfolders:
    # Get a list of all files (including videos and images) in the subfolder
    files_in_subfolder = [f.name for f in os.scandir(subfolder) if f.is_file()]
    
    # Check if there are any video files in the subfolder
    video_files_present = any(file.lower().endswith(('.mp4', '.avi', '.mkv', '.mov')) for file in files_in_subfolder)
    
    if video_files_present:
        # If there are video files, delete all image files in the subfolder
        image_files = [file for file in files_in_subfolder if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]
        
        for image_file in image_files:
            image_path = os.path.join(subfolder, image_file)
            os.remove(image_path)
            print(f"Deleted image file: {image_path}")
    else:
        print(f"No video files found in {subfolder}.")
