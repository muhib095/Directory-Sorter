# Project Name : Directory Sorter
# Date : 2024-08-26 -> 2024-08-27
# Author : Muhib Ullah 

# Using operating system dependent functionality like reading or writing to the file system, creating and deleting files or directories
import os 

# Allows you to do high-level operations on a file, such as copy, create, and remote operations
import shutil

# Path Example -> C:\Users\i5 12Th Gen\Downloads

# Ask the user for the folder they want organized
path = input("Enter Path: ").strip()

# Check if the provided path is a directory
if not os.path.isdir(path):
    print("Not a valid directory.")
else:
    # Iterate over each item in the specified directory
    for item in os.listdir(path):
        # Construct the full item path
        item_path = os.path.join(path, item)
        
        # Skip directory
        if os.path.isdir(item_path):
            continue
        
        # Get the file extension and define the destination directory
        file_extension = item.split('.')[-1] if '.' in item else 'no_extension'
        dest_dir = os.path.join(path, file_extension)
        
        # Create the destination directory if it does not exist
        if not os.path.exists(dest_dir):
            os.makedirs(dest_dir)
        
        # Define the destination path
        dest_path = os.path.join(dest_dir, item)
        
        # Move the item to the destination path
        try:
            shutil.move(item_path, dest_path)
            print(f"Moved {item} to {dest_path}")
        except Exception as e:
            print(f"Failed to move {item}: {e}")
    
    print("Files have been moved successfully.")