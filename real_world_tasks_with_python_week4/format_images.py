#!/usr/bin/env python3
import os
from PIL import Image

im_path = "/home/student-02-1f4c06ebd92c/supplier-data/images"
out_path = "/home/student-02-1f4c06ebd92c/supplier-data/images"

for imagepath in os.listdir(im_path):
        if imagepath in (".DS_Store", "README", "LICENSE"):
                continue
        else:
                f, e = os.path.splitext(imagepath)
                inputpath = os.path.join(im_path, imagepath)
                fulloutpath = out_path + "/" +  f + ".jpeg"
                im = Image.open(inputpath)
                im.resize((600,400)).convert("RGB").save(fulloutpath, "JPEG")
