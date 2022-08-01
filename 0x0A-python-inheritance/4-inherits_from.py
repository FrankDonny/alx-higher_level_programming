#!/usr/bin/python3
"""inherits_from module"""


def inherits_from(obj, a_class):
    """
    :return: returns True is obj inherits from a_class,
    False otherwise
    """
    return issubclass(type(obj), a_class) and type(obj) != a_class
