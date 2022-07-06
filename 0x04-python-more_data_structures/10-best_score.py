#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    a_dictionary = dict(a_dictionary)
    maxi = max(a_dictionary)
    return maxi
