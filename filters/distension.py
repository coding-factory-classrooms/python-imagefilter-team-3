import cv2
import numpy
import logger


def distension(image, file_name):
    filter_name = 'Distension'
    logger.log(filter_name, file_name)
    dilate = numpy.ones((5, 5), numpy.uint8)
    image_distension = cv2.dilate(image, dilate, iterations=2)
    return image_distension

