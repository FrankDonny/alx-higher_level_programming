#!/usr/bin/python3
"""Square class"""


class Square:
    """The size of the square initialization method"""
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position
        """The size must be an in else raise an exception"""
        if not isinstance(self.__size, int):
            raise TypeError("size must be an integer")
        else:
            """The size must be gt or eq to 0 else raise an exception"""
            if self.__size < 0:
                raise ValueError("size must be >= 0")

        if not isinstance(self.__position, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")

    """method that returns the area of a square"""
    def area(self):
        return self.__size * self.__size

    @property
    def position(self):
        return self.__size

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or (value[0] < 0 or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if isinstance(value, str):
            raise TypeError("size must be an integer")
        self.__size = value

    def my_print(self):
        if self.__size == 0:
            print(" ")
        for j in range(self.__position[1]):
            print()
        for i in range(self.__size):
            print(f"{' ' * self.__position[0]}", end="")
            print(f"{'#' * self.__size}")
