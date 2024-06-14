import os
import shutil

# Define the source root directory where all the folders are located
source_root = r"C:\Users\stefa\OneDrive\Dokumente\GitHub\faceAI\faceAI\data\test\test_no_face"

# Define the target directory where the "images" folders should be copied
target_directory = r"C:\Users\stefa\OneDrive\Dokumente\GitHub\faceAI\faceAI\data\test\no_face\images"

# Create the target directory if it doesn't exist
os.makedirs(target_directory, exist_ok=True)

# Loop through all directories in the source root
for folder_name in os.listdir(source_root):
    folder_path = os.path.join(source_root, folder_name)
    
    # Check if it's a directory
    if os.path.isdir(folder_path):
        images_folder_path = os.path.join(folder_path, "images")
        
        # Check if the "images" folder exists in the current directory
        if os.path.exists(images_folder_path) and os.path.isdir(images_folder_path):
            # Define the destination path
            destination_path = target_directory
            
            # Copy the contents of the "images" folder to the target directory
            for item in os.listdir(images_folder_path):
                s = os.path.join(images_folder_path, item)
                d = os.path.join(destination_path, item)
                if os.path.isdir(s):
                    shutil.copytree(s, d, dirs_exist_ok=True)
                else:
                    shutil.copy2(s, d)
            print(f"Copied contents of {images_folder_path} to {destination_path}")
        else:
            print(f"No 'images' folder found in {folder_path}")

            
        
