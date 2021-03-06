#!/usr/bin/python3
"""
This module contains the function matrix_mul
"""


def matrix_mul(m_a, m_b):
    """
    Description: Function to compute the matrix multiplication
    m_a: the first matix
    m_b: the second matrix
    raises TypeError, ValueError when encounter error
    """

    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    for i in m_a:
        if not isinstance(i, list):
            raise TypeError("m_a must be a list of lists")
        if len(i) != len(m_a[0]):
            raise TypeError("each row of m_a must be of the same size")
    for j in m_b:
        if not isinstance(j, list):
            raise TypeError("m_b must be a list of lists")
        if len(j) != len(m_b[0]):
            raise TypeError("each row of m_b must be of the same size")

    if m_a == [] or [x for x in m_a] == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or [y for y in m_b] == [[]]:
        raise ValueError("m_b can't be empty")

    for inner in m_a:
        for a in inner:
            if not isinstance(a, int or float):
                raise TypeError("m_a should contain only integers or floats")
    for inner1 in m_b:
        for b in inner1:
            if not isinstance(b, int or float):
                raise TypeError("m_b should contain only integers or floats")

    result = []
    for row in range(len(m_a)):
        list1 = []
        for col in range(len(m_b)):
            num = 0
            for k in range(len(m_b)):
                num += m_a[row][k] * m_b[k][col]
            list1.append(num)
        result.append(list1)
    return result
