#!/usr/bin/python3
def print_last_digit(number):
    last_num = str(number)[-1]
    print("{:d}".format(int(last_num)), end="")
    return int(last_num)
