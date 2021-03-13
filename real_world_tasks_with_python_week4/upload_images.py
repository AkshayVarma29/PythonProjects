#!/usr/bin/env python3
import requests
import os

url = "http://35.225.160.197/upload/"
im_path = "/home/student-02-1f4c06ebd92c/supplier-data/images"
for imagepath in os.listdir(im_path):
        if imagepath in (".DS_Store", "README", "LICENSE"):
                continue
        else:
                inputpath = os.path.join(im_path, imagepath)
                with open (inputpath, 'rb') as im:
                        r = requests.post(url, files={'file' : im})
