#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix == [[]]:
        print()
        return
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
                print("{:d}".format(matrix[i][j]), end=" " if j < len(matrix[i])-1 else "\n")

    if j < len(matrix[i])-1)
        print("{:d}".format(matrix[i][j]), end="")
    else:
        print("{:d}".format(matrix[i][j]), end=" ")
            