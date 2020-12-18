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

# Thanks to the command line '-i', the method 'listdir' return a list of the directory 'imgs'
files = os.listdir(inputdirectory)

# For each file of the directory 'imgs', we apply three filters on it and save it in the directory 'output'
for file_name in files:
    print(file_name)

    image = cv2.imread(inputdirectory + '/' + file_name)

    image = grey.grey(image, file_name)

    image = distension.distension(image, file_name)

    image = blurred.blur(image, file_name)

    cv2.imwrite(outputdirectory + '/' + file_name, image)


# Display on console the content of the file 'images.log'
logger.dump_log()

try:
    with os.scandir(args['entry']) as entries:
        for files in entries:
            path = f'{args["output"]}{file_name}'
            image = cv2.imread(f'{args["entry"]}{file_name}')
            image = blurred.distension.grey.modify_img(image,args["filtre_to_apply"])
            blurred.distension.grey.save_image(image,path)
            blurred.distension.grey.image_nbr += 1
except NameError:
    print("no entry for a directory or no filters found")

