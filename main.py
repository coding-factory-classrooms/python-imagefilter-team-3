import os
import logger
import cv2
from filters import grey, distension, blurred
import sys

input_dir = 'imgs'

a = {}

args = sys.argv

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


for file_name in files:
    print(file_name)

    image = cv2.imread(inputdirectory + '/' + file_name)

    image = grey.grey(image, file_name)

    image = distension.distension(image, file_name)

    image = blurred.blur(image, file_name)

    cv2.imwrite(outputdirectory + '/' + file_name, image)


logger.dump_log()




