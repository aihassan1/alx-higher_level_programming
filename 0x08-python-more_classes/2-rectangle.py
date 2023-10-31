#!/usr/bin/python3
""" create a class for a rec"""


class Rectangle:
    """creates a rec"""

    def __init__(self, width=0, height=0):
        """initilize parameters """
        self.width = width
        self.height = height

    @property
    def width(self):
        """get width"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """set width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """height getter """
        return (self.__height)

    @height.setter
    def height(self, value):
        """height setter """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """defines area of rec"""
        area = (self.width * self.height)
        return (area)

    def perimeter(self):
        """calculates para of rec"""
        if self.width == 0 or self.height == 0:
            return (0)
        para = (2 * (self.width + self.height))
        return (para)
