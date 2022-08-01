#!/usr/bin/python3
"""
BaseGeometry class module with a subclass Rectangle
"""


BaseGeometry = __import__("7-base_geometry").BaseGeometry

class Rectangle(BaseGeometry):
    """Rectangle class inheriting from super class BaseGeometry"""
    def __init__(self, width, height):
        """check validation of the width and height"""
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height
