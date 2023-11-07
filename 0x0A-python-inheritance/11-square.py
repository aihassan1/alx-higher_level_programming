#!/usr/bin/python3
"""Defines a square  that inherits Rectangle."""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """defines a square"""

    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """calculates area """
        return (self.__size * self.__size)

    def __str__(self):
        """for string def"""
        return ("[Square] {}/{}".format(self.__size, self.__size))
