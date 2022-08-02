#!/usr/bin/python3
"""add all command line arguments to a list and save them to a file"""
from sys import argv
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

length = len(argv)
ls = []
for i in range(1, length):
    ls.append(argv[i])

filename = "add_item.json"
save_to_json_file(ls, filename)