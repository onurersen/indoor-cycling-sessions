# !/usr/bin/env python
# title           : extract_session_info.py
# description     : Extracts session info from each cycling session and writes session file
# author          : Berat Onur Ersen (onurersen@gmail.com)
# date            : 20190219
# version         : 1.0
# usage           : python extract_session_info.py <folder_path>
# notes           : 
# python_version  : 3.6.5  
# ==============================================================================
import cv2
import numpy as np
import pytesseract
import sys
import os
import glob
import shutil
import datetime
import re
import traceback
from PIL import Image

numbers = re.compile(r'(\d+)')


def numerical_sort(value):
    parts = numbers.split(value)
    parts[1::2] = map(int, parts[1::2])
    return parts


def main():
    try:

        try:
            os.makedirs("../report")
        except FileExistsError:
            print("report directory already exists, emptying...")
            shutil.rmtree("../report", ignore_errors=True)
            os.makedirs("../report")

        # takes session folder path as argument
        if len(sys.argv) == 1:
            folder = "../enhanced"
        else:

            folder = sys.argv[1]

        files = [i for i in sorted(os.listdir(folder), key=numerical_sort) if i.lower().endswith(".png")]
        for file in files:
            report_file = open(os.path.join("../report", "session_info.txt"), "a+")
            existing_image_path = os.path.join(folder, file)
            extracted_text = get_string_from_text(existing_image_path)
            print("data being read from " + existing_image_path)
            activity_date = datetime.datetime.strptime(existing_image_path[find_str(existing_image_path, "201"):find_str(existing_image_path, ".png")], '%Y_%m_%d')
            formatted_activity_date = datetime.date.strftime(activity_date, "%d-%m-%Y")
            report_file.write("DATE " + formatted_activity_date + "\n")
            report_file.write(extracted_text + "\n")
            report_file.write("----------------------" + "\n")
            report_file.close()

            for aux_file in glob.glob("../*.png"):
                os.remove(aux_file)

    except IOError:
        traceback.print_exc()


def find_str(full, sub):
    sub_index = 0
    position = -1
    for ch_i, ch_f in enumerate(full):
        if ch_f.lower() != sub[sub_index].lower():
            position = -1
            sub_index = 0
        if ch_f.lower() == sub[sub_index].lower():
            if sub_index == 0:
                position = ch_i

            if (len(sub) - 1) <= sub_index:
                break
            else:
                sub_index += 1

    return position


def get_string_from_text(input_img_path):
    # Read image with opencv
    result = pytesseract.image_to_string(Image.open(input_img_path), config='-psm 6')
    text = "\n".join([ll.rstrip() for ll in result.splitlines() if ll.strip()])
    return text


if __name__ == '__main__':
    main()





