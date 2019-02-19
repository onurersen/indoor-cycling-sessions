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
from PIL import Image

def main():
    try:

        try:
            os.makedirs("report")
        except FileExistsError:
            print("report directory already exists, emptying...")
            shutil.rmtree("report", ignore_errors=True)
            os.makedirs("report")

        # takes session folder path as argument
        if len(sys.argv) == 1:
            folder = "enhanced"
        else:
            folder = sys.argv[1]

        files = [i for i in os.listdir(folder) if i.lower().endswith("enhanced.png")]
        for file in files:
            existing_image_path = os.path.join(folder, file)
            # new_image_path = os.path.join(folder,os.path.splitext(file)[0] + "_enhanced" + os.path.splitext(file)[1])
            extracted_text = get_string_from_text(existing_image_path, folder + "/")
            report_file = open(os.path.join("report", "session_info.txt"), "a+")
            print(extracted_text)
            report_file.write(extracted_text + "\n")
            report_file.write("----------------------" + "\n")
            report_file.close()

            for aux_file in glob.glob("*.png"):
                os.remove(aux_file)

    except IOError:
        traceback.print_exc()

def get_string_from_text(input_img_path, input_folder):
    # Read image with opencv
    input_image = cv2.imread(input_img_path)
    input_image = cv2.cvtColor(input_image, cv2.COLOR_BGR2GRAY)
    kernel = np.ones((1, 1), np.uint8)
    input_image = cv2.dilate(input_image, kernel, iterations=1)
    input_image = cv2.erode(input_image, kernel, iterations=1)
    cv2.imwrite(input_folder + "removed_noise.png", input_image)
    cv2.imwrite(input_folder + "thres.png", input_image)
    result = pytesseract.image_to_string(Image.open(input_folder + "thres.png"), config='-psm 6')
    text = "\n".join([ll.rstrip() for ll in result.splitlines() if ll.strip()])
    return text

if __name__ == '__main__':
    main()

