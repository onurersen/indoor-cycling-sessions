# !/usr/bin/env python
# title           : enhance_image_contrast.py
# description     : Increases image contrast to make text clearer for img2text
# author          : Berat Onur Ersen (onurersen@gmail.com)
# date            : 20190218
# version         : 1.0
# usage           : python enhance_image_contrast.py <folder_path>
# notes           :
# python_version  :3.6.5
# ==============================================================================
from PIL import Image, ImageEnhance
import os
import sys


def main():
    try:

        try:
            os.makedirs("enhanced")
        except FileExistsError:
            print("cropped directory already exists, emptying...")
            shutil.rmtree("enhanced", ignore_errors=True)

        # takes session folder path as argument
        if len(sys.argv) == 1:
            folder = "cropped"
        else:
            folder = sys.argv[1]

        files = [i for i in os.listdir(folder) if i.lower().endswith("_cropped.png")]
        for file in files:
            existing_image_path = os.path.join(folder, file)
            new_image_path = os.path.join("enhanced",
                                          os.path.splitext(file)[0] + "_enhanced" + os.path.splitext(file)[1])
            image = Image.open(existing_image_path)
            enhancer = ImageEnhance.Contrast(image)
            enhanced_image = enhancer.enhance(4.0)
            enhanced_image.save(new_image_path)

    except IOError:
        traceback.print_exc()


if __name__ == '__main__':
    main()


