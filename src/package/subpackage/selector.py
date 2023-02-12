from pathlib import Path

def name_prompt(path, old_new, folder_file):
    """Prompts the user for the name of a new or existing file or folder.
    Repeats prompt if an old folder doesn't exist, or a new folder does exist.
    Returns a tuple of a name and its valid path."""
    while True:
        name = input(f"Enter {old_new} {folder_file} name: ")
        test_path = Path(path / name)

        if old_new == "OLD" and not test_path.exists():
            print(f"No such {folder_file} exists --> please retry.")

        elif old_new == "NEW" and test_path.exists():
            print(f"\"{name}\" already exists --> please retry.")

        else:
            failsafe = input(f"You selected: \"{name}\" --> proceed? (Y/N): ")

            if failsafe.lower() in ["y", "yeah", "yep", "yes", "yup"]:
                return name, test_path

            print(f"\"{name}\" discarded --> please retry.")
