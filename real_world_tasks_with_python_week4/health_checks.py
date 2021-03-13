#!/usr/bin/env python3

import psutil
import socket
import emails
import os
import time

def health_check():
        # Use a breakpoint in the code line below to debug your script.
        cpu_usage = psutil.cpu_percent(interval=0.1)
        disk_usage = 100 - psutil.disk_usage("/").percent
        localdns = socket.gethostbyname('localhost')
        ava_mem = psutil.virtual_memory().free/2**20

        subject1 = ""
        if cpu_usage > 80:
                subject1 = "Error - CPU usage is over 80%"
        if disk_usage < 20:
                subject1 = "Error - Available disk space is less than 20%"
        if localdns != '127.0.0.1':
                subject1 = "Error - localhost cannot be resolved to 127.0.0.1"
        if ava_mem < 500:
                subject1 = "Error - Available memory is less than 500MB"
        if subject1 != "":
                sender = "automation@example.com"
                receiver = "{}@example.com".format(os.environ.get('USER'))
                subject = subject1
                body = "Please check your system and resolve the issue as soon as possible."

                message = emails.generate_health(sender, receiver, subject, body)
                emails.send(message)

if __name__ == '__main__':
        while True:
                health_check()
                time.sleep(60)
