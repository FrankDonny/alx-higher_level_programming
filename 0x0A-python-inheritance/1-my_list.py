#!/usr/bin/python3
"""
containing Mylist module
"""


class MyList(list):
    """Mylist class inherits from the list class"""
    def __init__(self):
        """initialize the class"""
        super(MyList, self).__init__()

    def print_sorted(self):
        """prints out the sorted list"""
        print(sorted(self))
