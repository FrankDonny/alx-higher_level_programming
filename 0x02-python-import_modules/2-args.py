#!/usr/bin/python3
import sys


def arg():
    length = len(sys.argv)
    return length - 1


count = 0

if len(sys.argv) <= 1:
    print("{} arguments.".format(arg()))
elif len(sys.argv) == 2:
    count += 1
    print("{} argument:".format(arg()))
    print("{}: {}".format(count, sys.argv[1]))
else:
    print("{} arguments:".format(arg()))
    for i in sys.argv:
        if i == sys.argv[0]:
            continue
        if len(sys.argv) > 2:
            count += 1
            print("{}: {}".format(count, i))
