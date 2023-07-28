import pathlib
import sys
import os
# PIL is the Pillow module a Python Imaging Library (Fork)
from PIL import Image

folder = sys.argv[1]
new_folder = sys.argv[2]

print(f"folder: {folder}, new_folder: {new_folder}")

if os.path.exists(new_folder):
    print(f"{new_folder} already exist, proceeding anyway..")
else:
    os.mkdir(new_folder)

# loop through the folder
for items in os.listdir(folder):
    img = Image.open(f"{folder}\\{items}")
    # convert image to png
    filename, ext = os.path.splitext(items)
    outfile = filename + ".png"
    # save to the new folder
    img.save(f"{new_folder}\\{outfile}")



