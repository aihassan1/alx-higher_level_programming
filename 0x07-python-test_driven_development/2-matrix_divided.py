#!/usr/bin/python3
"""

this module for the ""matrix_devide"" function

"""


def matrix_divided(matrix, div):
    """
    matrix_divided : devide each element of a matrix (list of lists )
    by a divider
    elements should be ints or floats
    all rows has to be the same length
    returns a float rounded to 2 dicimal places
    """
    # check if the list is a list of lists of integers or floats
    # check each member to be int or float
    for _list in matrix:
        if isinstance(_list, list):
            for member in _list:
                if not isinstance(member, (int, float)):
                    raise TypeError("""\
matrix must be a matrix (list of lists) of integers/floats\
""")
        else:
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")

    # check the size
    first_row_len = len(matrix[0])
    for row in matrix:
        if len(row) != first_row_len:
            raise TypeError("Each row of the matrix must have the same size")

    # check if dev is an int or float
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # check if dev is not zero
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # dived the matrix after passing all the checks
    matrix_result = []
    for row in matrix:
        new_row = []
        for element in row:
            new_ele = [round(element / div, 2)]
            new_row.append(new_ele)

        matrix_result.append(new_row)

    return (matrix_result)


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/2-matrix_divided.txt")
