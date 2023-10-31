#!/usr/bin/python3
"""
module to design a function that add two ints or floats
the function name is  "add_integer"
takes 2 args which could be ints or floats
"""


def add_integer(a, b=98):
    """
    add two ints or floats and returns an int
    args: a: the first arg, b: the second arg
    returns : the sum of two args
    """

    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")

    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")

    return (int(a) + int(b))


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
