import cv2


def grey(image):
    image_grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return image_grey


