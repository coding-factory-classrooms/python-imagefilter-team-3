import cv2


def blur(image):
    image_blur = cv2.GaussianBlur(image, (15, 15), 0)
    return image_blur






