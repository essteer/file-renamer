"""Bulk file renaming tool. Provides the option to rename all files in a folder
according to a sequence of numbers from an optional starting point, or to rename
files based on their metadata creation time.
Files within a folder should be examined and backed up first to catch exceptions."""
import package.series_renamer as series
import package.metadata_renamer as metadata

print("""This tool provides two options:
a) rename a folder and its entire contents with a custom number sequence; or
b) extract file metadata to rename files according to their creation date.""")

method = ""
OPTIONS = ("x", "a", "b")

while True:
    while method.lower() not in OPTIONS:
        print("")
        method = input("Select option 'a' or 'b', or type 'x' to quit: ")
    if method.lower() == OPTIONS[0]:
        exit()
    elif method.lower() == OPTIONS[1]:
        # run series_renamer tool
        series.renamer()
    elif method.lower() == OPTIONS[2]:
        # run metadata_renamer tool
        metadata.renamer()
    # TODO in Hong Kong folder, focus only on DSC and SAM files for metadata

    method = ""
    print("")
    print("""Would you like to process another folder? You can:
    a) rename a folder and its entire contents with a custom number sequence; or
    b) extract file metadata to rename files according to their creation date.""")

# TODO add an lstrip() method to process phone photos
# TODO add a regex method
# TODO update both renamer tools to use GUI instead of PATH at point of user selection
