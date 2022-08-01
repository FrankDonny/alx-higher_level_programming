#!/usr/bin/python3
"""is_kind_of_class module"""


def is_kind_of_class(obj, a_class):
    """

    :param obj:
    :param a_class:
    :return: True if is instance, else False otherwise
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
