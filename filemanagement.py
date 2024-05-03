import os
import sys

def rename_files(folder_path):
    try:
        # Get list of files in the folder
        files = os.listdir(folder_path)

        # Prompt for confirmation
        print(f"Are you sure you want to rename {len(files)} files in '{folder_path}'? (y/n): ", end="")
        confirm = input().strip().lower()

        if confirm != 'y':
            print("Operation cancelled.")
            return

        # Iterate through each file
        for i, filename in enumerate(files, start=1):
            # Construct the new file name
            new_filename = f"{filename}"

            # Construct the full path of the file
            old_path = os.path.join(folder_path, filename)
            new_path = os.path.join(folder_path, new_filename)

            # Rename the file
            os.rename(old_path, new_path)

            print(f"Renamed {filename} to {new_filename}")

        print("All files have been successfully renamed.")
    except FileNotFoundError:
        print(f"Error: Folder '{folder_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script_name.py <folder_path>")
        sys.exit(1)

    folder_path = sys.argv[1]
    rename_files(folder_path)
