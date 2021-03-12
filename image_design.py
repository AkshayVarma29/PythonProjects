#!/usr/bin/env python3
import os
from PIL import Image

im_path = "/home/user/images"
out_path = "/opt/icons"

for imagepath in os.listdir(im_path):
	if imagepath == ".DS_Store":
		continue
	else:
		inputpath = os.path.join(im_path, imagepath)
		fulloutpath = os.path.join(out_path, imagepath)
		im = Image.open(inputpath)
		im.rotate(270).resize((128,128)).convert("RGB").save(fulloutpath, "JPEG")
