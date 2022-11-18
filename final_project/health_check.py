#!/usr/bin/env python3
"""Checks system utilization and connection and sends warning email if there is any problem"""
import psutil
import shutil
import emails
import socket

def send_message(header):
    message = emails.generate_email("automation@example.com", "username@example.com",
                                    header,
                                    "Please check your system and resolve the issue as soon as possible",
                                    None)
    emails.send_email(message)

localhost = socket.gethostbyname('localhost')
total_disk, used_disk,free_disk =shutil.disk_usage("/")
free_ram =  psutil.virtual_memory()[1]

if localhost !="127.0.0.1":
    send_message("Error - localhost cannot be resolved to 127.0.0.1")
if psutil.cpu_percent(5) > 0.8:
    send_message("Error - CPU usage is over 80%")
if  free_disk/total_disk< 0.2:
    send_message("Error - Available disk space is less than 20%")
if free_ram < 500:
    send_message("Error - Available mempry is less than 500MB")
