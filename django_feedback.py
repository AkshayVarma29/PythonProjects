#!/usr/bin/env python3
import os
import requests

fb_path = "/data/feedback"

for fb in os.listdir(fb_path):
        if fb == ".DS_Store":
                continue
        else:
                in_path = os.path.join(fb_path, fb)
                fb_list = []
                with open(in_path, "rb") as file:
                        content = []
                        for line in file.readlines():
                                content.append(line)
                        content_dict = {}
                        content_dict['title'] = content[0]
                        content_dict['name'] = content[1]
                        content_dict['date'] = content[2]
                        content_dict['feedback'] = content[3]
                        response = requests.post("http://url/feedback/", data=content_dict)
                        if not response.ok:
                                raise Exception("GET failed with status code {}".format(response.status_code))
                        else:
                                continue
