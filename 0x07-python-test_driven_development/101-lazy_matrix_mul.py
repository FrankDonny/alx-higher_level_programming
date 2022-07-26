#!/usr/bin/python3
import numpy as np
"""
This function multiplies 2 matrices
with the use of NUMPY
"""


def lazy_matrix_mul(m_a, m_b):
    aa = np.array(m_a)
    bb = np.array(m_b)
    cc = aa.dot(bb)
    return cc
