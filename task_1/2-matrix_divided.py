#!/usr/bin/python3
"""
    This module defines a function that divides all elements
    of a matrix
"""


def matrix_divided(matrix, div):
    """ Returns a new matrix holding the division of all
        elements if a matrix
    Args:
        matrix - (list of int/float) first argument
        div - (int/float): second argument (Divisor)
    Raises:
        TypError: if arg1 is not a matrix (list of lists) of int/floats
        TypError: if  each row of the matrix is not the same size
        TypError: if div is not an integer or flaot
        ZerodivisionError : if div is equal to 0
    """
    if type(matrix) != list or not all(isinstance(row, list) for row in matrix)\
            or not all(isinstance(i, (int, float)) for row in matrix for i in row):
        raise TypeError('matrix must be a matrix (list of lists)'
                        ' of integers/floats')

    row_len = len(matrix[0])
    if not all(len(row) == row_len for row in matrix):
        raise TypeError('Each row of the matrix must have the same size')

    if not (isinstance(div, (int, float))):
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')

    return [[round(i / div, 2) for i in row] for row in matrix]
