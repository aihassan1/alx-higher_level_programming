#!/usr/bin/python3
"""Defines a class Rectangle that inherits from BaseGeometry."""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    defines a rectangle using basegeometry
    Args:
        width (int): The width of the new Rectangle.
        height (int): The height of the new Rectangle.
    """

    def __init__(self, width, height):
        super().__init__()
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("heiggh", height)
        self.__height = height

