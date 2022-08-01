#!/usr/bin/python3
"""is_same_class module"""


def is_same_class(obj, a_class):
    """
    :param obj:
    :param a_class:
    :return: True if same, else False otherwise
    """
    if isinstance(obj.__class__, a_class):
        return True
    else:
        return False
