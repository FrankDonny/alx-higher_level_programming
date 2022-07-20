#!/usr/bin/python3
"""Square class"""


class Square:
    """The size of the square initialization method"""
    def __init__(self, size=0):
        self.__size = size

    """method that returns the area of a square"""
    def area(self):
           return self.__size * self.__size

    @property
    def size(self):
        return self.__size
    
    @size.setter
    def size(self, value):
        """The size must be an in else raise an exception"""
        if not isinstance(self.__size, int or float):
            raise TypeError("size must be an integer")
        else:
            """The size must be gt or eq to 0 else raise an exception"""
            if self.__size < 0:
                raise ValueError("size must be >= 0")
        self.__size = value

    def __lt__(self, other):
        """
        Check if square is less than other
        """
        return self.size < other.size

    def __le__(self, other):
        """
        Check if square is less than or equal to the other
        """
        return self.size <= other.size

    def __eq__(self, other):
        """
        Check if square is equal to the other
        """
        return self.size == other.size

    def __ne__(self, other):
        """
        Check if square is not equal to the other
        """
        return self.size != other.size

    def __ge__(self, other):
        """
        Check if square is greater than or equal to the other
        """
        return self.size >= other.size

    def __gt__(self, other):
        """
        Check if square is greater than the other
        """
        return self.size > other.size
