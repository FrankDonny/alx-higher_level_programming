#!/usr/bin/python3
"""
This module contain the function lazy_matrix_mul
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    This function multiplies 2 matrices
    with the use of NUMPY
    """

    aa = np.array(m_a)
    bb = np.array(m_b)
    cc = aa.dot(bb)
    return cc
