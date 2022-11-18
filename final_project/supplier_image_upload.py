#!/usr/bin/env python3
"""Uploads images to site using Django framework"""

import requests
import os
home_dir=os.path.expanduser("~")
print(home_dir)
img_dir=os.path.join(home_dir,"supplier-data/images","")
print(img_dir)
url = "http://34.66.151.250//upload/"

for file in os.listdir(img_dir):
    if ".jpeg" in file:
        with open (img_dir+file,'rb') as opened:
            r=requests.post(url,files={"file":opened})

