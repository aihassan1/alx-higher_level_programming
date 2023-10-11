#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    copied_matrix = [row[:] for row in matrix]

    edited_matrix = [[x**2 for x in row] for row in copied_matrix]

    return edited_matrix
