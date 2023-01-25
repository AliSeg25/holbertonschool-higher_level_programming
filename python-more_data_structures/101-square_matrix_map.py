#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    nv_matrix = []
    for i in range(len(matrix)):
        nv_matrix.append(list(map(lambda x: x ** 2, matrix[i])))
    return nv_matrix
