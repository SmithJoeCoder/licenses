import numpy as np
import glob
import cv2
import random


def GaussianNoise(src, means, sigma, percetage):
    NoiseImg = src
    NoiseNum = int(percetage*src.shape[0]*src.shape[1])
    for j in range(NoiseNum):
        randX = random.randint(0, src.shape[0]-1)
        randY = random.randint(0, src.shape[1]-1)
        NoiseImg[randX, randY] = NoiseImg[randX, randY]+random.gauss(means, sigma)
        if NoiseImg[randX, randY] < 0:
            NoiseImg[randX, randY] = 0
        elif NoiseImg[randX, randY] > 255:
            NoiseImg[randX, randY] = 255
    return NoiseImg


all_data = glob.glob("temp/*.jpg")

for i in all_data:
    image = cv2.imread(i)
    result = GaussianNoise(image, 2, 4, 0.8)

    cv2.resizeWindow('Averaged', 94, 24)
    cv2.imshow("result", result)
    cv2.waitKey()
