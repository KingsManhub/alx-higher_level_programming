#!/usr/bin/python3

try:
    def print_matrix_integer(matrix=[[]]):
        for i in range(3):
            for j in range(3):
                print("{:3d}".format(matrix[i][j]), end="")
            print("")
except TypeError:
    print("")
