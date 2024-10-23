import os
import shutil
import random

def split_and_copy_images(source_folder, destination_folder, label, train_ratio=0.7, test_ratio=0.15, valid_ratio=0.15):
    # Ensure ratios sum up to 1
    if train_ratio + test_ratio + valid_ratio != 1.0:
        print("The ratios must sum up to 1!")
        return
    
    # Ensure the destination folder structure exists
    train_folder = os.path.join(destination_folder, 'train')
    test_folder = os.path.join(destination_folder, 'test')
    valid_folder = os.path.join(destination_folder, 'valid')
    
    for folder in [train_folder, test_folder, valid_folder]:
        if not os.path.exists(folder):
            os.makedirs(folder)
            print(f"Created folder: {folder}")

    # Get all files in the source folder
    files = [file for file in os.listdir(source_folder) if file.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif'))]
    
    total_files = len(files)
    if total_files == 0:
        print(f"No image files found in source folder: {source_folder}")
        return
    
    print(f"Total {total_files} images found.")
    
    # Shuffle the files randomly
    random.shuffle(files)
    
    # Split the dataset
    train_split = int(train_ratio * total_files)
    test_split = int(test_ratio * total_files)
    
    train_files = files[:train_split]
    test_files = files[train_split:train_split + test_split]
    valid_files = files[train_split + test_split:]
    
    # Helper function to copy files with the new label
    def copy_files(file_list, target_folder):
        for file_name in file_list:
            # Construct the full file path
            source_file = os.path.join(source_folder, file_name)
            
            # Add the label to the file name
            new_file_name = label + file_name
            
            # Construct the destination file path
            destination_file = os.path.join(target_folder, new_file_name)
            
            # Copy the file to the target folder
            try:
                shutil.copy(source_file, destination_file)
                print(f"Copied {file_name} to {destination_file}")
            except Exception as e:
                print(f"Failed to copy {file_name}. Error: {str(e)}")
    
    # Copy files to respective folders
    copy_files(train_files, train_folder)
    copy_files(test_files, test_folder)
    copy_files(valid_files, valid_folder)

# Example usage
source_folder = r"C:\Users\Anvesha\Downloads\Pistols.v1-resize-416x416.tensorflow\export"  # Replace with the folder path where your 3000 images are stored
destination_folder = r"dataset"  # Replace with the folder path where you want train/test/valid folders created
label = "1_"  # Label to be added to each image file

# Call the function to split, rename, and copy images
split_and_copy_images(source_folder, destination_folder, label)