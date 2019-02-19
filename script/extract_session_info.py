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
from PIL import Image

def main():
    try:

        folder = sys.argv[1]
        files = [i for i in os.listdir(folder) if i.lower().endswith("enhanced.png")]

        for file in files:
            existing_image_path = os.path.join(folder, file)
            # new_image_path = os.path.join(folder,os.path.splitext(file)[0] + "_enhanced" + os.path.splitext(file)[1])
            extracted_text = get_string_from_text(existing_image_path,folder+"/")
            f = open("session_info.txt", "a+")
            print(extracted_text)
            f.write(extracted_text + "\n")
            f.write("----------------------" + "\n")
            f.close()
                        
    except IOError:
        traceback.print_exc()

def get_string_from_text(img_path,src_path):
    # Read image with opencv
    img = cv2.imread(img_path)

    # Convert to gray
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply dilation and erosion to remove some noise
    kernel = np.ones((1, 1), np.uint8)
    img = cv2.dilate(img, kernel, iterations=1)
    img = cv2.erode(img, kernel, iterations=1)

    # Write image after removed noise
    cv2.imwrite(src_path + "removed_noise.png", img)

    # Write the image after apply opencv to do some ...
    cv2.imwrite(src_path + "thres.png", img)
    print(src_path + "thres.png")
    # Recognize text with tesseract for python
    result = pytesseract.image_to_string(Image.open(src_path + "thres.png"),config='-psm 6')

    text = "\n".join([ll.rstrip() for ll in result.splitlines() if ll.strip()])
    return text

if __name__ == '__main__':
    main()
