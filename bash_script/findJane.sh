#!/bin/bash
# Creates oldFiles.txt.
> oldFiles.txt
# Finds filenames, that should be changed, in list.txt
files=$(grep " jane " ../data/list.txt | cut -d ' ' -f 3)
# Appends filenames to oldFiles.txt
for file in $files;do
  if test -e $(dirname $(pwd))$file; then echo $(dirname $(pwd))$file>>oldFiles.txt ; else e$
done
