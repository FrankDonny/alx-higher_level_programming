#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_list = matrix.copy()
    for mems in new_list:
        for i in range(0, len(new_list)):
            mems[i] = mems[i] ** 2
    return new_list


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

new_matrix = square_matrix_simple(matrix)
print(new_matrix)
print(matrix)
