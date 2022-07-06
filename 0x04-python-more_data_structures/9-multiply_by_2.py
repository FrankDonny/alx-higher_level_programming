#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    a_dictionary = dict(a_dictionary)

    for key, value in sorted(a_dictionary.items()):
        print(f"{key}: {value}")

def multiply_by_2(a_dictionary):
    a_dictionary = dict(a_dictionary)
    for k, v in a_dictionary.items():
        a_dictionary[k] = v * 2
    return a_dictionary
