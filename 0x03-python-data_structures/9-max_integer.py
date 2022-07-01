#!/usr/bin/python3
def max_integer(my_list=[]):
    my_list.sort()
    for i in my_list:
        i = my_list[-1]
        return i
