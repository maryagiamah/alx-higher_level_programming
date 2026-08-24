#!/usr/bin/python3
"""Contains lazy_matrix_mul"""


import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Multiplies two matrices"""

    if not isinstance(m_a, list):
        raise TypeError('m_a must be a list')
    if not isinstance(m_b, list):
        raise TypeError('m_b must be a list')

    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    if m_a == [] or m_a == [[]]:
        raise ValueError('m_a can\'t be empty')
    if m_b == [] or m_b == [[]]:
        raise ValueError('m_b can\'t be empty')

    row_a = len(m_a[0])
    row_b = len(m_b[0])

    if not all(len(row) == row_a for row in m_a):
        raise TypeError("each row of m_a must be of the same size")
    if not all(isinstance(col, (int, float)) for row in m_a for col in row):
        raise TypeError("m_a should contain only integers or floats")

    if not all(len(row) == row_b for row in m_b):
        raise TypeError("each row of m_b must be of the same size")
    if not all(isinstance(col, (int, float)) for row in m_b for col in row):
        raise TypeError("m_b should contain only integers or floats")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    arr_a = np.array(m_a)
    arr_b = np.array(m_b)

    return np.matmul(arr_a, arr_b).to_list()
