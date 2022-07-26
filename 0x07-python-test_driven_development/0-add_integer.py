#!/usr/bin/python3
"""
Description: This file contains the add integer module
"""


def add_integer(a, b=98):

    """
    a: is the first variable to hold the first element
    b: is the second variable to hold the second element with a placeholdeer
    of 98
    """

    if isinstance(a, int) or isinstance(a, float):
        """if a is float, typecast it to integer"""
        a = int(a)
    if isinstance(b, int) or isinstance(b, float):
        """if b is float, typecast it to integer"""
        b = int(b)
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    """return the result of the addition"""
    return a + b
