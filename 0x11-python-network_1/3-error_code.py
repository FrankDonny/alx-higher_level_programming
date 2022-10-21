#!/usr/bin/python3
import urllib.request
from sys import argv

req = urllib.request.Request(argv[1])
try:
    with urllib.request.urlopen(req) as response:
        html = response.read()
        print(html.decode('utf-8'))
except urllib.error.HTTPError as e:
    print(f'Error code: {e.code}')
