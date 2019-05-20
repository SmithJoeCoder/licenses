import cv2 as cv
import glob
import numpy as np
import os

all_data = glob.glob("temp/*.jpg")
for i in all_data:
    src = cv.imread(i)

    blurred_5 = np.hstack([cv.bilateralFilter(src, 9, 41, 41)])
    blurred_7 = np.hstack([cv.bilateralFilter(src, 9, 41, 41)])
    blurred_9 = np.hstack([cv.bilateralFilter(src, 9, 41, 41)])

    # cv2.bilateralFilter(src, 5, 21, 21),
    #
    # cv2.bilateralFilter(src, 7, 31, 31),
    #
    # cv2.bilateralFilter(src, 9, 41, 41)

    # cv.namedWindow("Bilateral", cv.WINDOW_NORMAL)

    # cv.resizeWindow('Bilateral', 94, 24)

    # cv.imshow("Bilateral", blurred)

    # cv.waitKey(0)
    filename = i.split("\\")[1].split(".")[0]
    # cv.imshow("result", blurred)
    # cv.waitKey()
    if not os.path.exists("temp/" + filename + "_bilateral9" + ".jpg"):
        cv.imwrite("temp/" + filename + "_bilateral5" + ".jpg", blurred_5)
        cv.imwrite("temp/" + filename + "_bilateral7" + ".jpg", blurred_7)
        cv.imwrite("temp/" + filename + "_bilateral9" + ".jpg", blurred_9)
