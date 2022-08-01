#!/usr/bin/python3
def add_attribute(obj, name, value):
    """function to add an attribute to an object if possible
    obj: the object
    name: the object name
    value: the object value
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
