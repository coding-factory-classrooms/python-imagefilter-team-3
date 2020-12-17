import os
import cv2
from filters import grey, distension, blurred
import sys

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

a = {}


args = sys.argv
print(args)
for i in range(0, len(args)):
    arg = args[i]
    print(i)
    print(arg)
    if args[i] == '-i':
        inputdirectory = args[i + 1]
    if args[i] == '-o':
        outputdirectory = args[i + 1]

    if arg == '-h':
        print("-h,----help")
        print("-i, --input-dir <directory>")
        print("-o, --output-dir <directory>")



files = os.listdir(inputdirectory)
print(files)

for f in files:
    print(f)

    image = cv2.imread(inputdirectory + '/' + f)

    image = grey.grey(image)

    image = distension.distension(image)

    image = blurred.blur(image)

    cv2.imwrite(outputdirectory + '/' + f,image)






