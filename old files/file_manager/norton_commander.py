
import os
from file_manager.sort_dir import sort_folder
GREEN = "\033[92m"
RESET = "\033[0m"

def display_directory_contents(path, indent=4):
    try:
        entries = [entry for entry in os.listdir(path) if not entry.startswith('.')]
    except OSError as e:
        print(f"Error reading directory {path}: {e}")
        return

    print("Current directory:", os.path.abspath(path))
    print('folder composition: ')

    for entry in entries:
        entry_path = os.path.join(path, entry)
        if os.path.isdir(entry_path):
            print("  " * indent + f"[{entry}]")
        else:
            print("  " * indent + entry)

    while True:
        choice = input("Enter folder name to explore, type '..' to go up, or 'sort' to sort (press Enter to exit): ")
        if not choice:
            break
        elif choice == '..':
            parent_path = os.path.dirname(path)
            if parent_path != path:
                display_directory_contents(parent_path, indent)
                break
            else:
                print("Already at the top level.")
        elif choice.lower() == 'sort':
            sort_choice = input("Want to sort the current folder? (y/n): ")
            if sort_choice.lower() == 'y':
                sort_folder(path)
                print(f"{GREEN}Folder was sorted{RESET}")
                display_directory_contents(path, indent)
            elif sort_choice.lower() == 'n':
                continue
            else:
                print("Invalid input. Please enter 'y' or 'n'.")
        elif os.path.isdir(os.path.join(path, choice)):
            display_directory_contents(os.path.join(path, choice), indent + 1)
        else:
            print("Invalid input. Try again.")

