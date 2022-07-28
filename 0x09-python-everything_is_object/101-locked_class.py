#!/usr/bin/python3
"""define a locked class"""


class LockedClass(object):
    """apart from first_name instance, no new instance is to be created"""
    __slots__ = ['first_name']
