#!/usr/bin/python3
"""reading file module"""


def read_file(filename=""):
    """This function reads the content of a file"""
    with open(filename, 'r', encoding='utf-8') as theFile:
        print(theFile.read(), end="")
