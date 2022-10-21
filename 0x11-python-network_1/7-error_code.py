#!/usr/bin/python3
"""Python script that sends a request and displays
the body of the response (decoded in utf-8)"""
import requests
from sys import argv

if __name__ == '__main__':
    req = requests.get(argv[1])
    if req.status_code >= 400:
        print(f"Error code: {req.status_code}")
    else:
        print(f"{req.text}")
