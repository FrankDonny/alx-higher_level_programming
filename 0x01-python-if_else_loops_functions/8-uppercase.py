#!/usr/bin/python3
def uppercase(str):
    result = ""
    for i in str:
        if ord(i) in range(97, 123):
            caps = ord(i) - 32
            result += chr(caps)
        else:
            result += i
    print("{}".format(result))
