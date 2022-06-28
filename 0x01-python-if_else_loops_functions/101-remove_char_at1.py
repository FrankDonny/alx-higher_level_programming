#!/usr/bin/python3
def remove_char_at(str, n):
    string = ""
    if n > len(str) or n < 0:
        return str
    else:
        for i in str:
            if i == str[n]:
                continue
            string += i
    return string
