#!/usr/bin/env python3
"""Checks connection status"""
import requests
import socket
def check_localhost():
    localhost = socket.gethostbyname('localhost')
    return localhost == "127.0.0.1"
def check_connectivity(site):
    request = requests.get(site)
    return request.status_code == 200