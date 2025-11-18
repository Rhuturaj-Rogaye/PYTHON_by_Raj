import os

def print_files_only(dir_path):
    try:
        for name in os.listdir(dir_path):
            full_path = os.path.join(dir_path, name)
            if os.path.isfile(full_path):
                print(name)
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    path = input("Enter directory path (or press Enter for current directory): ").strip() or "."
    print_files_only(path)