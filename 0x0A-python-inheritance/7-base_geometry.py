#!/usr/bin/python3
"""BaseGeometry class module"""


class BaseGeometry:
    """BaseGeometry class"""
    def area(self):
        """raises error message"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """integer validator"""
        if not isinstance(value, int):
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
