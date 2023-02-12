from pathlib import Path
from PIL import Image
from PIL.ExifTags import TAGS
import package.subpackage.parser as parser
import shutil

def renamer():
    dir_path = Path.home() / "Pictures" / "TESTING"

    print("Processing files, please wait...")

    for path in dir_path.rglob("*.*"):

        image = Image.open(path)
        exif = image.getexif()

        # Create a dictionary of the image metadata:
        exif_dict = {TAGS[k]: v for k, v in exif.items() if k in TAGS}
        # Extract the creation datetime as a variable:
        creation_date = exif_dict["DateTime"]
        # Send the creation datetime to parser() to process the string:
        new_filename = parser.date_parser(creation_date) + path.suffix

        # TODO the path.replace() method returns a Windows error - file in use
        # path.replace(new_filename)
        new_path = Path(dir_path / new_filename)
        shutil.copy2(path, new_path)

        # TODO the path.unlink() method returns a Windows error - file in use
        # path.unlink()
