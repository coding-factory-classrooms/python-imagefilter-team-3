import cv2
import logger


def blur(image, file_name):
    """
    Apply a blur filter on the pictures
    :param image: the picture which will be modify
    :param file_name:
    :return: the picture modify
    """
    filter_name = 'Blurred'
    logger.log(filter_name, file_name)
    image_blur = cv2.GaussianBlur(image, (15, 15), 0)
    return image_blur






