import image as image
from PIL import Image
import cv2
import numpy as np
import matplotlib.pyplot as plt
import pandas
import sys
import glob


def analyze_veins(img):
    for i in range(0, img.shape[0]):
        for j in range(0, img.shape[1]):
            #gre = img[i, j, 2] / img[i, j, 1] * 100
            if img[i, j, 2] < 30 or img[i, j, 0] < 130:
                img[i, j] = [0, 0, 0]
            else:
                img[i, j] = [0, 255, 255]
    return img


if __name__ == '__main__':
    files = glob.glob('../img/*')
    for file in files:
        img = cv2.imread(file)
        col_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        artifact = analyze_veins(col_img)
        artifacts_folder = '../artifacts/' + file.split('/')[2]
        cv2.imwrite(artifacts_folder, artifact)
