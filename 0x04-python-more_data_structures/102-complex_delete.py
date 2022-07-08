#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if bool(value) == 0:
        return
    a_dictionary_copy = a_dictionary.copy()
    for k in a_dictionary_copy.keys():
        if value == a_dictionary.get(k):
            del a_dictionary[k]
    return a_dictionary
