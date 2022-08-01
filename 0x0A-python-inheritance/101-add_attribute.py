#!/usr/bin/python3
"""
function to add an attribute to an object if possible
"""


def add_attribute(obj, name, value):
    """obj: the object
    name: the object name
    value: the object value
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
