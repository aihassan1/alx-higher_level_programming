#!/usr/bin/python3
""" Module for base geometry. """


class BaseGeometry:
    """ Base class for geometric shapes."""

    def area(self):
        """calculates area - not defined yet"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """checks if the value type is int """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
