#!/usr/bin/python3
"""Write a function that divides all elements of a matrix."""


def matrix_divided(matrix, div):
    """
    Matrix division function
    @matrix: matrix to be divided composed of ints ot floats
    @div: integer that will divide the matrix
    """
    if not all(isinstance(el, list) for el in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if not all(len(el) == len(matrix[0]) for el in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if type(div) not in [int, float]:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(el / div, 2) for el in liste] for liste in matrix]
