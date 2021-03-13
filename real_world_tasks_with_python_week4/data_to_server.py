#!/usr/bin/env python3
import os
import requests

fr_path = "/home/student-02-1f4c06ebd92c/supplier-data/descriptions/"
im_path = "/home/student-02-1f4c06ebd92c/supplier-data/images"
im_list = []
for imagepath in os.listdir(im_path):
        if imagepath == ".DS_Store":
                continue
        else:
                inputpath = os.path.join(im_path, imagepath)
                image = os.path.basename(inputpath)
                if ".jpeg" in image:
                        im_list.append(image)
images_list = sorted(im_list)

i = 0
for fr in os.listdir(fr_path):
        if fr == ".DS_Store":
                continue
        else:
                in_path = os.path.join(fr_path, fr)
                with open(in_path, "rb") as file:
                        content = []
                        for line in file.readlines():
                                content.append(line)
                        content_dict = {}
                        content_dict['name'] = content[0]
                        content_dict['weight'] = int(content[1][:-4])
                        content_dict['description'] = content[2]
                        content_dict['image_name'] = images_list[i]
                        i += 1
                        response = requests.post("http://35.225.160.197/fruits/", data=content_dict)
                        if not response.ok:
                                raise Exception("GET failed with status code {}".format(response.status_code))
                        else:
                                continue
