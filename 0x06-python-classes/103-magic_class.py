#!/usr/bin/python3
"""Define MagicClass"""
import math


class MagicClass:
    """initialize the class"""
    def __init__(self, radius=0):
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """get the area"""
        return (self.__radius ** 2) * math.pi

    def circumference(self):
        """get the circumference"""
        return 2 * math.pi * self.__radius
