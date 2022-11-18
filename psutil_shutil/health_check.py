#!/usr/bin/env python3
""" Import build-in and custom modules to check system utilization and connection"""
import shutil
import psutil
import network
site_name = "http://www.google.com"

# Verifies that there's enough free space on disk.
def check_disk_usage(disk):
    du = shutil.disk_usage(disk)
    free = du.free / du.total * 100
    return free > 20

# Verifies that there's enough unused CPU.
def check_cpu_usage():
    usage = psutil.cpu_percent(1)
    return usage < 75

# If there's not enough disk, or not enough CPU, print an error.
# Output information about connection.
if not check_disk_usage('/') or not check_cpu_usage():
    print("ERROR!")
elif network.check_localhost() and network.check_connectivity(site_name):
    print("Everything ok")
else:
    print("Network checks failed")

