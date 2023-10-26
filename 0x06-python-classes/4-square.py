#!/usr/bin/python3
"""defines a Square"""


class Square:
    """ Defines a square.  """

    def __init__(self, size=0):
        """ Initializes a new Square instance with a given size. """
        self.size = size

    @property
    def size(self):
        """        Getter method for the size property.        """
        return self.__size

    @size.setter
    def size(self, value):
        """ Setter method for the size property """
        if isinstance(value, int):
            if value >= 0:
                self.__size = value
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """ Calculates the area of the square  """
        return self.__size * self.__size
