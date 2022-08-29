#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    if len(matrix) > 0:
        for i in range(3):
            for j in range(3):
                print("{:3d}".format(matrix[i][j]), end="")
            print("")
    else:
        print("")

