"""
A python tool to resize images 
Usage:
    python fit_image.py --images xxxx 
if you wanna set image resolution please use this command :
    python fit_image.py --images xxxx --width 1920 --height 1080 
"""

import os
from PIL import Image
import argparse
import re


def resize_image(image_path, args):
    img = Image.open(image_path)
    img = img.resize([args.width, args.height], Image.BILINEAR)
    img.save(image_path)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--images", type=str, default="",
                        help="the location of image folder")
    parser.add_argument('--image', type=str, default="", help="a image")
    parser.add_argument('--width', type=int, default=1920,
                        help="the target image width")
    parser.add_argument('--height', type=int, default=1080,
                        help="the target image hegiht")
    args = parser.parse_args()
    print(args)
    if args.images:
        for root, dirs, files in os.walk(args.images):
            for idx, file in enumerate(files):

                if file.endswith('.jpg') or file.endswith('.png') or file.endswith('.gif'):
                    print('Resize {} image'.format(idx + 1))
                    resize_image(os.path.join(root, file), args)
        print('Finish resize')
    elif args.image:
        print('Resize image:', args.image)
        resize_image(args.image, args)
        print('Finish resize')
    else:
        print("Please check the path of images")
