#!/usr/bin/python3
"""append to file module"""


def append_write(filename="", text=""):
    """This function appends texts to a file without overwriting it"""
    with open(filename, 'a', encoding='utf-8') as myFile:
        return myFile.write(text)
