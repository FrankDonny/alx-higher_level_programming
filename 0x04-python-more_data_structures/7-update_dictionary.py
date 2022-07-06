#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    a_dictionary = dict(a_dictionary)

    for key, value in sorted(a_dictionary.items()):
        print(f"{key}: {value}")


def update_dictionary(a_dictionary, key, value):
    a_dictionary = dict(a_dictionary)
    for k,v in a_dictionary.items():
        a_dictionary[key] = value
    return a_dictionary
