#!/usr/bin/python3
def load_from_json_file(filename):
    """this function reads from a json file"""
    with open(filename, encoding='utf-8') as myFile:
        new = myFile.read()
    return new
