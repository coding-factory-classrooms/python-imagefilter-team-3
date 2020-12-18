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

try: # 'entry' et 'filter_to_apply ne peuvent pas définir a l'exception de
    with os.scandir(args['entry']) as entries:#ouvrir le répertoire sous forme de liste
        for files in entries:# le fichier représente des images
            path = f'{args["output"]}{file_name}'
            image = cv2.imread(f'{args["entry"]}{file_name}') # réference des images
            image = blurred.distension.grey.modify_img(image,args["filter_to_apply"])
            blurred.distension.grey.save_image(image,path)
            blurred.distension.grey.image_nbr += 1
except NameError:
    print("no entry for a directory or no filters found")

