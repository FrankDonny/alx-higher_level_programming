#!/usr/bin/python3
"""Python script to display X-Request-Id value"""
import requests
from sys import argv

if __name__ == '__main__':
    req = requests.get(argv[1])
    html = req.headers
    print(html['X-Request-Id'])
