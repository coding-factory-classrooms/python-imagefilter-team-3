import cv2
import numpy


def distension(image):
    dilate = numpy.ones((5, 5), numpy.uint8)
    image_distension = cv2.dilate(image, dilate, iterations=2)
    return image_distension


