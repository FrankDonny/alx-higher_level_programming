#!/usr/bin/python3
"""writing to file module"""


def write_file(filename="", text=""):
    """
    This function open a file in write mode and write to it
    and return the number of characters
    """
    with open(filename, 'w', encoding='utf-8') as myFile:
        return myFile.write(text)
