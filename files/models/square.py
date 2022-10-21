#!/usr/bin/python3
"""The Square module in the model package"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """The Square class inheriting from Rectangle class"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute"""

        if args and len(args) != 0:
            ls = [x for x in args]
            if len(ls) == 1:
                self.id = ls[0]
            elif len(ls) == 2:
                self.size = ls[1]
            elif len(ls) == 3:
                self.x = ls[2]
            elif len(ls) == 4:
                self.y = ls[3]
        else:
            for k, v in kwargs.items():
                if k == "id":
                    self.id = v
                elif k == "size":
                    self.size = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        """return a dictionary representation of instances"""
        _dict = {"size": self.size, "x": self.x, "y": self.y, "id": self.id}
        return _dict

    def __str__(self):
        """returns a human-readable string format of the class"""
        return f"[Square] ({self.id}) {super(Square, self).x}/" \
               f"{super(Square, self).y} - {self.width}"

    @property
    def size(self):
        """the size property"""
        return self.width

    @size.setter
    def size(self, value):
        """the size setter"""
        self.width = value
        self.height = value
