# File Renamer

## Overview

This script is designed to rename all files within a specified folder. It's a simple Python script that allows batch renaming of files.

## Usage

To use this script, follow these steps:

1. **Clone Repository**: Clone this repository to your local machine.
2. **Navigate to Directory**: Open a terminal or command prompt and navigate to the directory where the script is located.
3. **Run Script**: Execute the script by providing the folder path as a command-line argument. For example:

    ```
    python script_name.py <folder_path>
    ```

    Replace `<folder_path>` with the path to the folder containing the files you want to rename.

4. **Confirmation**: The script will prompt you to confirm the renaming operation. Type 'y' to proceed or 'n' to cancel.

5. **Renaming Process**: If confirmed, the script will iterate through each file in the specified folder, renaming them according to the specified pattern.

6. **Completion**: Once the renaming process is complete, the script will display a message indicating that all files have been successfully renamed.

## Notes

- **Error Handling**: The script includes basic error handling to handle cases where the specified folder does not exist or if any other errors occur during the renaming process.

- **Caution**: Ensure that you have a backup of your files before running the script, especially if renaming large numbers of files, to prevent accidental data loss.
