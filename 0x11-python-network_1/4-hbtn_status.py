#!/usr/bin/python3
import requests

resp = requests.get("https://alx-intranet.hbtn.io/status")
print("Body response:")
print(f"\t- type: {type(resp.text)}")
print(f"\t- content: {resp.text}")
