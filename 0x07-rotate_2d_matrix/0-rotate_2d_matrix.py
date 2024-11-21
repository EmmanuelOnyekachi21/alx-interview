#!/usr/bin/python3
"""
A Script that contains a function which rotates a 2D matrix.

Complete 2D matrix rotation challenge
"""


def deep_copy(matrix):
    """Creates a deep copy of a given matrix"""
    matrix_cpy = []
    for row in matrix:
        row_cpy = []
        for column in row:
            row_cpy.append(column)
        matrix_cpy.append(row_cpy)
    return matrix_cpy


def rotate_2d_matrix(matrix):
    """Takes a given 2D matrix and rotates it in place to the right. """
    matrix_cpy = deep_copy(matrix)
    n = len(matrix)
    for row, columns in enumerate(matrix):
        for index in range(n):
            columns[index] = matrix_cpy[(n - index - 1)][row]
