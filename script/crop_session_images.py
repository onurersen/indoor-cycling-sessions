# !/usr/bin/env python
# title           : crop_session_images.py
# description     : Crops png images in target folder to prepare for contrast adjustment
# author          : Berat Onur Ersen (onurersen@gmail.com)
# date            : 20190218
# version         : 1.0
# usage           : python crop_session_images.py <folder_path>
# notes           :
# python_version  : 3.6.5
# ==============================================================================
from PIL import Image
import os
import sys
import shutil
import traceback


def main():
    try:

        try:
            os.makedirs("../cropped")
        except FileExistsError:
            print("cropped directory already exists, emptying...")
            shutil.rmtree("../cropped", ignore_errors=True)
            os.makedirs("../cropped")
        # takes session folder path as argument
        if len(sys.argv) == 1:
            folder = "../session"
        else:
            folder = sys.argv[1]

        files = [i for i in os.listdir(folder) if i.lower().endswith("png")]
        # iterate over files and crop to appropriate image size
        for file in files:
            existing_image_path = os.path.join(folder, file)
            new_image_path = os.path.join("../cropped",
                                          os.path.splitext(file)[0] + os.path.splitext(file)[1])
            img = Image.open(existing_image_path)
            (width, height) = img.size
            area = (0, height / 4 + height / 15, width, height - (height / 20))
            img = img.crop(area)
            img.save(new_image_path)
            print(existing_image_path + " cropped.")
    except IOError:
        traceback.print_exc()


if __name__ == '__main__':
    main()
