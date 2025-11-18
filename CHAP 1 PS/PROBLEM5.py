# Import the os module for interacting with the operating system
import os

# Function to print only files from a given directory
def print_files_only(dir_path):
    try:
        # Loop through each item in the directory
        for name in os.listdir(dir_path):
            # Get the full path of the item (directory + file name)
            full_path = os.path.join(dir_path, name)
            
            # Check if the item is a file (not a folder)
            if os.path.isfile(full_path):
                print(name)  # Print file name
    except Exception as e:
        # Handle errors (like invalid path or permission issues)
        print("Error:", e)

# Main execution block (runs only if file is executed directly)
if __name__ == "__main__":
    # Ask user to enter directory path (defaults to current directory if blank)
    path = input("Enter directory path (or press Enter for current directory): ").strip() or "."
    
    # Call function to print files from the given path
    print_files_only(path)

