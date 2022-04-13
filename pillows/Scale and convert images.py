#!/usr/bin/env python3

import os

from PIL import Image


def image_pillow(image_file_name):
    f, e = os.path.splitext(image_file_name)
    image_file = imagedir + "/" + image_file_name
    out_dir = "/home/student-04-04584c7c0f98/opt/icons/"
    outfile = out_dir + f + ".jpg"
    with Image.open(image_file) as im:
        print(im.mode)
        if im.mode in ["LA", "P"]:
            im.convert('RGB').resize((128, 128)).rotate(270).save(outfile, "JPEG")
        else:
            im.resize((128, 128)).rotate(270).save(outfile, "JPEG")


imagedir = "/home/student-04-04584c7c0f98/images"
if os.path.isdir(imagedir):
    for image in os.listdir(imagedir):
        if not image.startswith('.') and not image.endswith(".jpg"):
            image_pillow(image)
