from PIL import Image
import numpy as np
import sys
import os
import csv
import matplotlib.pyplot as plt
import cv2 as cv


#Useful function
def createFileList(myDir, format='.png'):  ##format can be anything like '.png. or '.jpeg',.....
    fileList = []
    print(myDir)
    for root, dirs, files in os.walk(myDir, topdown=False):
        for name in files:
            if name.endswith(format):
                fullName = os.path.join(root, name)
                fileList.append(fullName)
    return fileList

# load the original image
myFileList = createFileList("/directory_name")

for file in myFileList:
    print(file)
    img_file = Image.open(file)
    # print(img_file.show())

    # get original image parameters...
    width, height = img_file.size
    format = img_file.format
    mode = img_file.mode

    # Make image Greyscale
    img_grey = img_file.convert('L')
    img_grey.save('result.png')
    # img_grey.show()

    # Save Greyscale values
    value = np.asarray(img_grey.getdata(), dtype=np.int).reshape((img_grey.size[1], img_grey.size[0]))
    value = value.flatten()
    print(value)
    with open("img_pixels.csv", 'a') as f:
        writer = csv.writer(f)
        writer.writerow(value)
