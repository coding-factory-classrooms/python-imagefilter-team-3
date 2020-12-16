import cv2



def blur_picture():
    image = cv2.imread('imgs/photo_desert.jpg')
    image_blur = cv2.GaussianBlur(image,(15,15),0)

    image = cv2.imread('imgs/photo_montagne.jpg')
    image_blur2 = cv2.GaussianBlur(image, (15, 15), 0)

    image = cv2.imread('imgs/photo_ciel.jpg')
    image_blur3 = cv2.GaussianBlur(image, (15, 15), 0)

    image = cv2.imread('imgs/photo_ocean.jpg')
    image_blur4 = cv2.GaussianBlur(image, (15, 15), 0)

    cv2.imwrite('output/Blur/blur_desert.jpg', image_blur)
    cv2.imwrite('output/Blur/blur_montagne.jpg', image_blur2)
    cv2.imwrite('output/Blur/blur_ciel.jpg', image_blur3)
    cv2.imwrite('output/Blur/blur_ocean.jpg', image_blur4)



