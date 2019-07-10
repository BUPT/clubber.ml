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
    w, h = img.size
    if args.ratio > 0:
        w_hat = int(w * args.ratio)
        h_hat = int(h * args.ratio)
    else:
        if args.width > 0 and args.height > 0:
            w_hat = args.width
            h_hat = args.height
        elif args.width > 0 and args.height == 0:
            w_hat = args.width
            h_hat = int(w_hat / w * h)
        elif args.width == 0 and args.height > 0:
            h_hat = args.height
            w_hat = int(h_hat / h * w)
        else:
            print('please check options')
            w_hat = w
            h_hat = h
    img = img.resize([w_hat, h_hat], Image.BILINEAR)
    img.save(image_path)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--images", type=str, default="",
                        help="the location of image folder")
    parser.add_argument('--image', type=str, default="", help="a image")
    parser.add_argument('--width', type=int, default=1920,
                        help="the target image width")
    parser.add_argument('--height', type=int, default=0,
                        help="the target image hegiht")
    parser.add_argument('--ratio', type=float, default=0,
                        help="the ratio to resize image")
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
