import os
import cv2
from filters import grey, distension, blurred

input_dir = 'imgs'
files = os.listdir(input_dir)
print(files)

for f in files:
    print(f)

    image = cv2.imread(f'{input_dir}/{f}')

    image = grey.grey(image)

    image = distension.distension(image)

    image = blurred.blur(image)

    cv2.imwrite(f'output/{f}', image)