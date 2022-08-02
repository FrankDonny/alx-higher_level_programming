#!/usr/bin/python3
"""json module"""
import json


def save_to_json_file(my_obj, filename):
    """write a python str from json to a file"""
    with open(filename, 'w', encoding='utf-8') as myFile:
        myFile.write(json.dumps(my_obj))
