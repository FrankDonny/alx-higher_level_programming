#!/usr/bin/python3
"""finding the peak module"""


def find_peak(list_of_integers):
    """find the peak in a list"""
    if len(list_of_integers) == 0:
        return
    return max(list_of_integers)
