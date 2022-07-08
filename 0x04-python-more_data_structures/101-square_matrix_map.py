#!/usr/bin/python3
def my_func(matrix=[]):
    return list(map(lambda x: list(map(lambda y: y**2, x)), matrix))
