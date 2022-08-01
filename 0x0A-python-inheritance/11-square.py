#!/usr/bin/python3
"""square module"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class inheriting from Rectangle"""
    def __init__(self, size):
        """initializing size"""
        super().integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    def area(self):
        """implementing the area module"""
        return super().area()

    def __str__(self):
        return f"[Square] {self.__size}/{self.__size}"


s = Square(13)

print(s)
print(s.area())
