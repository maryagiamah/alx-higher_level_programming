#!/usr/bin/python3
"""
This is the "2-matrix_divided" module.
The 2-matrix_divided module supplies one function, matrix_divided(matrix, div).
"""


def matrix_divided(matrix, div):
    """Divides all elements in the matrix by div"""

    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    for row in matrix:
        if not isinstance (row, list):
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")

        if matrix[0] != len(row):
            raise TypeError("Each row of the matrix must have the same size")

        for i in row:
            if not isinstance(i, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of / integers/floats")

    return [[round(i / div, 2) for i in row] for row in matrix]

