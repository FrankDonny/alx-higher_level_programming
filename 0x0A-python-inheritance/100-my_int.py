#!/usr/bin/python3

class MyInt(int):
    def __init__(self, num):
        super(MyInt, self).__init__()
        self.num = num

    def rebel(self):
        return not self.num


my_i = MyInt(3)
print(my_i)
print(my_i == 3)
print(my_i != 3)
