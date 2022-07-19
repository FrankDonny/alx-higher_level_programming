#!/usr/bin/python3
"""Square class"""


class Square:
    """The size of the square initialization method"""
    def __init__(self, size=0):
        self.__size = size
        """The size must be an in else raise an exception"""
        if not isinstance(self.__size, int):
            raise TypeError("size must be an integer")
        else:
            """The size must be gt or eq to 0 else raise an exception"""
            if self.__size < 0:
                raise ValueError("size must be >= 0")

    """method that returns the area of a square"""
    def area(self):
        return self.__size * self.__size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if isinstance(value, str):
            raise TypeError("size must be an integer")
        else:
            self.__size = value

    def my_print(self):
        if self.__size == 0:
            print(" ")
        for i in range(self.__size):
            print(f"{'#' * self.__size}")
