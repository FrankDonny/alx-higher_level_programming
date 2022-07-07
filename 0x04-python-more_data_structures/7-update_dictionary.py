#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    a_dictionary = dict(a_dictionary)
    for k,v in a_dictionary.items():
        a_dictionary[key] = value
    return a_dictionary
