#!/usr/bin/python3
"""json reading file module"""
import json


def load_from_json_file(filename):
    """this function reads from a json file"""
    with open(filename, encoding='utf-8') as myFile:
        return json.load(myFile)
