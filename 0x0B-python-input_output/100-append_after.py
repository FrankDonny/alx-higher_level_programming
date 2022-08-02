#!/usr/bin/python3
"""appending string module"""


def append_after(filename="", search_string="", new_string=""):
    """appends new_string after a line when search_string is found
    in the current line
    """
    string = ""
    with open(filename, 'r', encoding='utf-8') as theFile:
        lines = []
        for line in theFile:
            lines.append(line)
            if search_string in line:
                lines.append(new_string)
        for i in lines:
            string += i

    with open(filename, 'w', encoding='utf-8') as wFile:
        return wFile.write(string)
