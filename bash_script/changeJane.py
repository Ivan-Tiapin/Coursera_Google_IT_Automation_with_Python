#!/usr/bin/env python3
"""Changes "jane" to "jdoe" in files name"""
import sys
import subprocess

old_files_list=sys.argv[1]
with open(old_files_list) as file:
  for line in file.readlines():
    old_line =line.strip()
    new_line = old_line.replace("jane","jdoe")
    subprocess.run("mv "+old_line+" "+new_line, shell=True)
