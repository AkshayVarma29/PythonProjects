#!/usr/bin/env python3
import os
from PIL import Image

### Define source and destination paths
im_path = "/home/user/images"
out_path = "/opt/icons"

### Traverse the Images in the source directory
for imagepath in os.listdir(im_path):
  
  ### Ignore .DS_Store file
	if imagepath == ".DS_Store":
		continue
	
  else:
    
    ### Get absolute paths
		inputpath = os.path.join(im_path, imagepath)
		fulloutpath = os.path.join(out_path, imagepath)
		im = Image.open(inputpath)
    
    ### Perform Operations on the Image and save as JPEG format
		im.rotate(270).resize((128,128)).convert("RGB").save(fulloutpath, "JPEG")
