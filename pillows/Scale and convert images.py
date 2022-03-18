#!/usr/bin/env python3

from PIL import Image
import os

def image_pillow(image_file_name):
    f, e = os.path.splitext(image_file_name)
    image_file = imagedir + "/" + image_file_name
    out_dir = "/home/student-04-04584c7c0f98/opt/icons/"
    outfile = out_dir + f + ".jpg"
    with Image.open(image_file) as im:
        print(im.mode)
        if im.mode in ["LA","P"]:
            im.convert('RGB').resize((128, 128)).rotate(270).save(outfile, "JPEG")
        else:
            im.resize((128, 128)).rotate(270).save(outfile, "JPEG")
    # try:
    #     with Image.open(image_file) as im:
    #         im.rotate(90)
    #         im.resize((128, 128))
    #         im.save(imagedir, "JPEG", optimize=True, quality=80 )
    # except OSError:
    #     print("cannot convert", image_file)

imagedir="/home/student-04-04584c7c0f98/images"
if os.path.isdir(imagedir):
    for image in os.listdir(imagedir):
        if not image.startswith('.') and not image.endswith(".jpg") :
            image_pillow(image)




