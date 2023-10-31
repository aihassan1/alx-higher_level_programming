#!/usr/bin/python3
"""
module that defines a Square
"""


def print_square(size):
    """
    prints a square based on the size number
    size: has to be an int
    """

    # Check if size is an int
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    # check if the size is > zero
    if size < 0:
        raise ValueError("size must be >= 0")

    # print the square with the char #
    for i in range(size):
        for j in range(size):
            print('#', end='')
        print('')


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/4-print_square.txt")
