# renamer.py
# Originally created to clean up photo files.
# Moves old folder files to new folder, under new names,
# with unique number suffixes in the same parent folder.
from pathlib import Path
import package.subpackage.iterator as it
import package.subpackage.selector as selector
import package.subpackage.sequencer as sequencer

def renamer():
    dir_path = Path.home() / "Pictures" / "TESTING"

    old_dirname, old_path = selector.name_prompt(dir_path, "OLD", "folder")

    while True:
        try:
            new_dirname, new_path = selector.name_prompt(dir_path, "NEW", "folder")
            new_path.mkdir()
            break
        except OSError:  # Catches invalid filename characters \/:*?"<>|
            print("Invalid name --> please retry with standard characters.")

    num0s = sequencer.n_zeroes()  # Prompts user to determine suffix digit length
    num = sequencer.n_start(num0s)  # Prompts user to determine starting sequence

    count = it.iterator(dir_path, old_path, new_dirname, num0s, num)
    print(f"{count:,d} files were renamed and moved to {new_path}.")

    try:
        old_path.rmdir()
        print("The original directory was emptied and has been deleted.")
    except OSError:
        print("The original directory still contains files, and has been preserved.")

# TODO add option for types of files, or all files
# TODO add bat functionality to run from Win+R
