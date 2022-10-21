#!/usr/bin/python3
"""Python script to display X-Request-Id value"""
import urllib.request
from sys import argv

if __name__ == '__main__':
    req = urllib.request.Request(argv[1])
    with urllib.request.urlopen(req) as response:
        html = response.headers
        print((html['X-Request-Id']).decode('utf-8'))
