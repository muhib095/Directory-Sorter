# Project Name : Directory Sorter
# Date : 2024-08-26 -> 2024-08-27
# Author : Muhib Ullah 

# Using operating system dependent functionality like reading or writing to the file system, creating and deleting files or directories
import os 

# Allows you to do high-level operations on a file, such as copy, create, and remote operations
import shutil

# Python GUI Tkinter
from tkinter import *

from tkinter import messagebox

# Path Example -> C:\Users\i5 12Th Gen\Downloads

def directory_sorter():

    # Get the folder they want organized
    path = entry1.get().strip()

    # Check if the provided path is a directory
    if not os.path.isdir(path):
        messagebox.showerror("Error", "Not a valid directory.")
        return
    
    try:
        # Iterate over each item in the specified directory
        for item in os.listdir(path):
            # Construct the full item path
            item_path = os.path.join(path, item)

            # Skip if it's a directory
            if os.path.isdir(item_path):
                continue

            # Get the file extension or use 'no_extension' if none
            file_extension = item.split('.')[-1] if '.' in item else 'no_extension'
            dest_dir = os.path.join(path, file_extension)

            # Create the destination directory if it does not exist
            if not os.path.exists(dest_dir):
                os.makedirs(dest_dir)

            # Define the destination path
            dest_path = os.path.join(dest_dir, item)

            # Move the item to the destination path
            shutil.move(item_path, dest_path)

        # Show success message
        messagebox.showinfo("Success", "Files have been moved successfully.")
    except Exception as e:
        # Show error message in case of failure
        messagebox.showerror("Error", f"An error occurred: {e}")

# Create a new window pop up
window = Tk()
window.title("Directory Sorter")
window.geometry('400x200')

# Create an entry widget to input the directory path
entry1 = Entry(window, width=50)
entry1.pack(pady=20)

# Create a button that starts the directory sorting
Button(window, text="Begin!", command=directory_sorter).pack()

# Start the GUI event loop
window.mainloop()        
