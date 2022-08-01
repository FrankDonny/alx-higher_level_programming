#!/usr/bin/python3
"""
BaseGeometry class module with a subclass Rectangle
"""


class BaseGeometry:
    """BaseGeometry class"""
    def area(self):
        """raises error message"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """integer validator"""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """Rectangle class inheriting from super class BaseGeometry"""
    def __init__(self, width, height):
        """check validation of the width and height"""
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height
