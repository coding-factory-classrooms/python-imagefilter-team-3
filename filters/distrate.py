import cv2
import numpy as np


def distrate_picture():
    image2 = cv2.imread('imgs/photo_ciel.jpg')
    kernel = np.ones((5, 5), np.uint8)
    image_distrate = cv2.dilate(image2, kernel, iterations=2)

    image2 = cv2.imread('imgs/photo_desert.jpg')
    kernel = np.ones((5, 5), np.uint8)
    image_distrate2 = cv2.dilate(image2, kernel, iterations=2)

    image2 = cv2.imread('imgs/photo_montagne.jpg')
    kernel = np.ones((5, 5), np.uint8)
    image_distrate3 = cv2.dilate(image2, kernel, iterations=2)

    image2 = cv2.imread('imgs/photo_ocean.jpg')
    kernel = np.ones((5, 5), np.uint8)
    image_distrate4 = cv2.dilate(image2, kernel, iterations=2)


    cv2.imwrite('output/Distrate/distrate_ciel.jpg', image_distrate)
    cv2.imwrite('output/Distrate/distrate_desert.jpg', image_distrate2)
    cv2.imwrite('output/Distrate/distrate_montagne.jpg', image_distrate3)
    cv2.imwrite('output/Distrate/distrate_ocean.jpg', image_distrate4)