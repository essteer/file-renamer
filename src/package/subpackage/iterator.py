from pathlib import Path

def iterator(dir_path, old_path, new_dirname, num0s, num, count=0):
    """Iterates over files in folder.
    Renames files and moves them to target folder.
    Returns integer of number of files processed."""
    print("Processing files, please wait...")

    for path in old_path.rglob("*.*"):
        # if path.suffix.lower() in [".gif", ".jpg", ".png"]:  # TODO this is preventing deletion of empty dir
        new_filename = f"{'_'.join(new_dirname.split())}_{str(num).zfill(num0s)}"
        new_path = Path(new_filename + path.suffix)
        path.replace(dir_path / new_dirname / new_path.name)
        num += 1
        count += 1

    return count

# for path in documents_dir.rglob("*.*"):
#     if path.suffix.lower() in [".png", ".jpg", ".gif"]:
#         path.replace(images_dir / path.name)
