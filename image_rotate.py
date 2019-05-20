import numpy as np
import glob
import cv2
import random

all_data = glob.glob("temp/*.jpg")

for i in all_data:
    image = cv2.imread(i, 0)
    rows, cols = image.shape
    M = cv2.getRotationMatrix2D((cols/2,rows/2),10,1)
    result = cv2.warpAffine(image, M, (cols, rows))

    cv2.resizeWindow('Averaged', 94, 24)
    cv2.imshow("result", result)
    cv.imwrite("temp/" + filename + "_bilateral5" + ".jpg", blurred_5)
    cv2.waitKey()
