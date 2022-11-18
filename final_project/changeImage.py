#!/usr/bin/env python3
"""Converts images to .jpeg format with 600x400 size"""

from PIL import Image
import os

home_dir=os.path.expanduser("~")
img_dir=os.path.join(home_dir,"supplier-data/images","")

# Searches for non-jpeg files and converts them if possible
for file in os.listdir(img_dir):
  if ".jpeg" not in file:
    try:
      image = Image.open(img_dir+file)
      image.convert("RGB").resize((600,400)).save(img_dir+file.split(".")[0]+".jpeg","jpeg")
      print("{} proceded".format(file))
    except:
      print("ERROR with {}".format(file))
