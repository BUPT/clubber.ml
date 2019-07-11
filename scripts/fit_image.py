"""
A python tool to resize images 
Usage:
    python fit_image.py --images xxxx 
if you wanna set image resolution ,please use this command :
    python fit_image.py --images xxxx --width 1920 --height 1080  or
    python fit_image.py --images xxxx --width 1920 or 
    python fit_image.py --images xxxx  --height 1080 
if you wanna set image resolution by ratio ,please use this command:
    python fit_image.py --images xxx --ratio 0.5

"""

import os
from PIL import Image
import argparse
import re


def chose_proper_resolution(args, old_width, old_height):
    """
    according the ratio or weight and hegiht to chose a proper resolution

    return the proper resolution

    """
    # use ratio to resize
    if args.ratio > 0:
        target_width = int(old_width * args.ratio)
        target_height = int(old_height * args.ratio)
    else:
        # use width or height to resize
        if old_width > args.width > 0 and old_height > args.height > 0:
            # when width and height both are set
            target_width = args.width
            target_height = args.height
        elif old_width > args.width > 0 and args.height == 0:
            # when only width is set
            target_width = args.width
            target_height = int(args.width / old_width * old_height)
        elif args.width and old_height > args.height > 0:
            # when olny height is set
            target_width = int(args.height / old_height * old_width)
            target_height = args.height
        else:
            # other cases, don't modify images
            target_width = old_width
            target_height = old_height

    return target_width, target_height


def resize_image(image_path, args):
    """
    According ratio or resolution to resize image and relpace source image
    """
    img = Image.open(image_path)
    old_width, old_height = img.size
    target_width, target_height = chose_proper_resolution(
        args, old_width, old_height)
    img = img.resize([target_width, target_height], Image.BILINEAR)
    img.save(image_path)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--images", type=str, default="",
                        help="the location of image folder")
    parser.add_argument('--image', type=str, default="", help="a image")
    parser.add_argument('--width', type=int, default=0,
                        help="the target image width (recommend 1920)")
    parser.add_argument('--height', type=int, default=0,
                        help="the target image hegiht(recommend 1080)")
    parser.add_argument('--ratio', type=float, default=0,
                        help="the ratio to resize image (recommend 0.7)")
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
