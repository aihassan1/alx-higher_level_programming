#!/usr/bin/python3
""" create a class for a rec"""


class Rectangle:
    """creates a rec"""
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """initilize parameters """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        rectangle_str = "\n".join([str(self.print_symbol) * self.__width] *
                                  self.__height)
        return rectangle_str

    def __repr__(self):
        return ("Rectangle({}, {})".format(self.__width, self.__height))

    def __del__(self):
        if Rectangle.number_of_instances != 0:
            Rectangle.number_of_instances -= 1

        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")

        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() == rect_2.area() or rect_1.area() > rect_2.area():
            return rect_1

        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        return (cls(size, size))
