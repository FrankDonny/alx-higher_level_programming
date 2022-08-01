#!/usr/bin/python3
"""Containing the MyInt module"""


class MyInt(int):
    """MyInt module class"""
    def __init__(self, num):
        """Initializing myInt class"""
        super(MyInt, self).__init__()
        self.num = num

    def __eq__(self, other):
        """revert the __eq__ dunder method"""
        return self.num != other

    def __ne__(self, other):
        """revert the __ne__ dunder method"""
        return self.num == other
