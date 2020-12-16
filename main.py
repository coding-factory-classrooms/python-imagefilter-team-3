import cv2

image = cv2.imread('imgs/photo_ciel.jpg')
image_grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

image = cv2.imread('imgs/photo_desert.jpg')
image_grey2 = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

image = cv2.imread('imgs/photo_montagne.jpg')
image_grey3 = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

image = cv2.imread('imgs/photo_ocean.jpg')
image_grey4 = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imwrite('output/grey_ciel.jpg', image_grey)
cv2.imwrite('output/grey_desert.jpg', image_grey2)
cv2.imwrite('output/grey_montagne.jpg', image_grey3)
cv2.imwrite('output/grey_ocean.jpg', image_grey4)