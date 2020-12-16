import cv2
import numpy


def distension_picture():
    image2 = cv2.imread('imgs/photo_ciel.jpg')
    dilate = numpy.ones((5, 5), numpy.uint8)
    image_distension = cv2.dilate(image2, dilate, iterations=2)

    image2 = cv2.imread('imgs/photo_desert.jpg')
    dilate = numpy.ones((5, 5), numpy.uint8)
    image_distension2 = cv2.dilate(image2, dilate, iterations=2)

    image2 = cv2.imread('imgs/photo_montagne.jpg')
    dilate = numpy.ones((5, 5), numpy.uint8)
    image_distension3 = cv2.dilate(image2, dilate, iterations=2)

    image2 = cv2.imread('imgs/photo_ocean.jpg')
    dilate = numpy.ones((5, 5), numpy.uint8)
    image_distension4 = cv2.dilate(image2, dilate, iterations=2)

    cv2.imwrite('output/Distension/distension_ciel.jpg', image_distension)
    cv2.imwrite('output/Distension/distension_desert.jpg', image_distension2)
    cv2.imwrite('output/Distension/distension_montagne.jpg', image_distension3)
    cv2.imwrite('output/Distension/distension_ocean.jpg', image_distension4)