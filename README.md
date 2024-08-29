# Directory-Sorter

Directory Sorter is a simple Python script designed to organize files within a specified directory. 

The script categorizes files based on their extensions and moves them into corresponding folders within the same directory.

![image](https://github.com/user-attachments/assets/44a78e03-b203-469c-ae85-d2574a603906)

![image](https://github.com/user-attachments/assets/d8c375ae-e08d-43c9-ac2c-5ed9effcaef6)

![image](https://github.com/user-attachments/assets/03f8e445-6547-4c18-9832-95f3da849f3d)

## Features

- Organizes files in a directory by their file extensions.

- Creates new folders for each file extension.

- Moves files into their respective extension folders.

## Dependencies

- os: Used for interacting with the operating system, such as reading or writing to the file system, and creating or deleting files or directories.

- shutil: Used for high-level operations on files like copying, creating, and moving files.

## How It Works

1. The user is prompted to enter the path of the directory they want to organize. Example:

```
/home/Muhib/Downloads
```

2. The script checks if the provided path is a valid directory. 

3. The script iterates over each item in the specified directory.

4. A success message is displayed for each file moved. If a file cannot be moved, an error message is shown.

5. Once all files are sorted, a completion message is displayed.

## Links

Contact @ ullah.muhib095@gmail.com

Linkedin @ https://www.linkedin.com/in/muhib095/
