#!/usr/bin/python3
import urllib.request
import urllib.parse
from sys import argv

url = argv[1]
value = {'email': argv[2]}
data = urllib.parse.urlencode(value)
data = data.encode('utf-8')
with urllib.request.urlopen(url, data) as response:
    print(response.read())
