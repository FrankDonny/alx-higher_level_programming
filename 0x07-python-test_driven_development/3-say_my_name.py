#!/usr/bin/python3
"""
This module contains the function to print out the full name
"""


def say_my_name(first_name, last_name=""):
    """
    This function print the fullname of a person
    if first_name is not sring, raise TypeError
    if Last_name is not string, raise TypeError
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print(f"My name is {first_name} {last_name}")
