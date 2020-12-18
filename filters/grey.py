import cv2
import logger


def grey(image, file_name):
    filter_name = 'Grey'
    logger.log(filter_name, file_name)
    image_grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return image_grey


