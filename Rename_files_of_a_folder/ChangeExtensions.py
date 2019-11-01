import os
import datetime

ext = ".png"
ext_end = ".jpg"

for root, dirs, files in os.walk("."):
    for file in files:
        if file[-4:].lower() in (ext):
            filename, _ = file.split(".")
            try:
                os.rename(os.path.join(root, file), os.path.join(root, filename + ext_end))
            except:
                pass
