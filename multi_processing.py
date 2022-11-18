#!/usr/bin/env python
"""Makes backup of <dir_name_original> content to <dir_name_backup> in concurrency"""
import subprocess
from multiprocessing import Pool
import os

src = "<dir_name_original>"
dest = "<dir_name_backup>"

# Makes backup
def run(dtc):
    print("Working on: " + dest + dtc)
    subprocess.call(["rsync", "-arq", src + dtc, dest + dtc])


if __name__ == "__main__":
    dtc = []
    # Creates list of directories that should be copied in parallel
    for root, dirs, files in os.walk(src):
        for dir in dirs:
            dtc.append(dir + "/")
        break

    # Creates amount of tasks, that should be run in parallel
    p = Pool(len(dtc))
    p.map(run, dtc)
