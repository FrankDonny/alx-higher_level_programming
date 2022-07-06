#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_list = []
    for mems in matrix:
        new_list.append(mems)

    for i in range(0, len(new_list)):
        new_list[i] = list(map(lambda x: x**2, new_list[i]))
    return new_list
