#!/usr/bin/python3
def remove_char_at(str, n):
    string = ""
    if n > len(str) or n < 0:
        return str
    else:
        for a in str:
            if a == str[n]:
                continue
            string += a
    return string
