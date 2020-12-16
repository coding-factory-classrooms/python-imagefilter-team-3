from filters import grey
from filters import distension
from filters import blurred
import os
import cv2


# grey.grey_picture()
#
# distension.distension_picture()
#
# blurred.blur_picture()

input_dir = 'imgs'
files = os.listdir(input_dir)
print(files)

for f in files:
    print(f)
    image = cv2.imread(f'{input_dir}/{f}')
    image = grey.grey(image)
    cv2.imwrite(f'output/{f}', image)

for f in files:
    print(f)
    image = cv2.imread(f'{input_dir}/{f}')
    image = distension.distension(image)
    cv2.imwrite(f'output/{f}', image)

for f in files:
    print(f)
    image = cv2.imread(f'{input_dir}/{f}')
    image = blurred.blur(image)
    cv2.imwrite(f'output/{f}', image)