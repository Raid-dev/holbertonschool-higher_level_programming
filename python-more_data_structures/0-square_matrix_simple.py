#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = matrix.copy()
    return [list(map(lambda x: x ** 2, row)) for row in new_matrix]
