#!/usr/bin/python3
print_sorted_dictionary = \
    __import__('6-print_sorted_dictionary').print_sorted_dictionary


def simple_delete(a_dictionary, key=""):
    a_dictionary = dict(a_dictionary)
    del a_dictionary[key]

    return a_dictionary