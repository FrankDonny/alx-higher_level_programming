#!/usr/bin/python3
"""The Rectangle module in the model package"""
import sys
from models.base import Base


class Rectangle(Base):
    """The Rectangle class inheriting from Base class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializing the instance variables"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def area(self):
        """returns the area of the Rectangle class"""
        return self.__width * self.__height

    def display(self):
        """displays the Rectangle figure when called"""

        [print("", file=sys.stdout) for y in range(self.y)]
        for i in range(self.__height):
            print(" " * self.__x, end="", file=sys.stdout)
            print("#" * self.__width, file=sys.stdout)

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute"""
        if not args:
            for k, v in kwargs.items():
                if k == "id":
                    self.id = v
                elif k == "width":
                    self.width = v
                elif k == "height":
                    self.height = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v
        else:
            ls = [x for x in args]
            if len(ls) == 1:
                self.id = ls[0]
            if len(ls) == 2:
                self.width = ls[1]
            if len(ls) == 3:
                self.height = ls[2]
            if len(ls) == 4:
                self.x = ls[3]
            if len(ls) == 5:
                self.y = ls[4]

    def to_dictionary(self):
        """return a dictionary representation of instances"""
        _dict = {
                "width": self.width,
                "height": self.height,
                "x": self.x,
                "y": self.y,
                "id": self.id
            }
        return _dict

    def __str__(self):
        """returns a human-readable string format of the class"""
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - \
{self.width}/{self.height}"

    @property
    def width(self):
        """width property"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """height property"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter"""
        if not isinstance(value, int):
            raise TypeError(f"height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """the x property"""
        return self.__x

    @x.setter
    def x(self, value):
        """the x setter"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """the y property"""
        return self.__y

    @y.setter
    def y(self, value):
        """the y setter"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
