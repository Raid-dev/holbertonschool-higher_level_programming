#!/usr/bin/python3
""" Matrix Division module """


def matrix_divided(matrix, div):
    """ Divides matrix """
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists) of integers
                /floats")
    new_matrix = []
    for i in range(len(matrix)):
        if not isinstance(matrix[i], list):
            raise TypeError("matrix must be a matrix (list of lists) of
                    integers/floats")
        for j in range(len(matrix[i])):
            if not isinstance(matrix[i][j], int) and not
            isinstance(matrix[i][j], float):
                raise TypeError("matrix must be a matrix (list of lists) of
                        integers/floats")
        if i != 0 and len(matrix[i]) != len(matrix[i-1]):
            raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    else:
        for i in range(len(matrix)):
            new_matrix.append([])
            for j in range(len(matrix[i])):
                new_matrix[i].append(round(matrix[i][j] / div, 2))
        return new_matrix
