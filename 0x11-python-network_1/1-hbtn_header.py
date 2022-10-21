#!/usr/bin/python3
import urllib.request
from sys import argv

req = urllib.request.Request(argv[1])
with urllib.request.urlopen(req) as response:
    html = response.headers
    print((html['X-Request-Id']).decode('utf-8'))
