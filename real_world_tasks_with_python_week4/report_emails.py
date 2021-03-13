#!/usr/bin/env python3

import json
import locale
import sys
import reports
import emails
import os
from datetime import date

today = date.today()
d2 = today.strftime("%B %d, %Y")

fr_path = "/home/student-02-1f4c06ebd92c/supplier-data/descriptions/"
data = "<br/>"
for fr in os.listdir(fr_path):
        if fr == ".DS_Store":
                continue
        else:
                in_path = os.path.join(fr_path, fr)
                with open(in_path, "r", encoding='utf-8') as file:
                        content = []
                        for line in file.readlines():
                                content.append(line)
                        data += "name: " + content[0] + "<br/>"
                        data += "weight: " + content[1] + "<br/>"
reports.generate("/tmp/processed.pdf", "Processed Update on " + d2, data)

sender = "automation@example.com"
receiver = "{}@example.com".format(os.environ.get('USER'))
subject = "Upload Completed - Online Fruit Store"
body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."

message = emails.generate(sender, receiver, subject, body, "/tmp/processed.pdf")
emails.send(message)
