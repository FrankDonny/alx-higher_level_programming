#!/usr/bin/python3
"""
This module contains contains the function to do
matrix division
"""


def matrix_divided(matrix, div):
    """
    Description: division of matrix
    matrix: this parameter receives the matrix the division should be used on
    div: is the number to be used to divide through the matrix
    Return: a new matrix
    """
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    for i in matrix:
        if not isinstance(i, list):
            raise TypeError(
                "matrix must be a matrix(list of lists) of integers/floats")
        for j in i:
            if not isinstance(j, int) and not isinstance(j, float):
                raise TypeError(
                    "matrix must be a matrix(list of lists) of integers/floats"
                    )

    if div == 0:
        raise ZeroDivisionError("division by zero")

    if len(matrix[0]) != len(matrix[1]):
        raise TypeError("Each row of the matrix must have the same size")

    new_matrix = []
    for i in range(len(matrix)):
        temp = []
        for j in matrix[i]:
            elem = j / div
            if isinstance(elem, float):
                elemf = round(elem, 2)
                temp.append(elemf)
            else:
                temp.append(elem)
        new_matrix.append(temp)
    return new_matrix
