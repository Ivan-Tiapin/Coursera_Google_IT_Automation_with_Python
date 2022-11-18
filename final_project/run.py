#!/usr/bin/env python3
"""Uploads descriptions to site using Django framework"""
import os
import requests

home_dir=os.path.expanduser("~")
texts_dir=os.path.join(home_dir,"supplier-data/descriptions","")
descritpions=[]
for file in os.listdir(texts_dir):
    print (file)
    with open(texts_dir+file) as text_file:
        text_dict={}
        text=text_file.readlines()
        text_dict['name']=text[0].strip()
        text_dict['weight']=int(text[1].strip().split(" ")[0])
        text_dict['description']=text[2].strip()
        text_dict['image_name']=file.split(".")[0]+".jpeg"
        print(type(text_dict['weight']))
        response = requests.post("http://34.66.151.250/fruits/", data=text_dict)
        print(response.ok)






