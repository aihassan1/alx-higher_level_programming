#!/usr/bin/python3
"""this is the module doc"""
from models.base import Base


class Rectangle(Base):
    """
    Defines a class to represent a rectangle, inheriting from the Base class.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes a rectangle object width, height, position, and id.
        """
        # check that the imnput is int
        Rectangle.check_int("width", width)
        Rectangle.check_int("height", height)
        Rectangle.check_int("x", x)
        Rectangle.check_int("y", y)

        # check for positve nums only
        Rectangle.check_positive("width", width)
        Rectangle.check_positive("height", height)
        Rectangle.check_positive("x", x)
        Rectangle.check_positive("y", y)

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """ Getter method for the width attribute."""
        return self.__width

    @width.setter
    def width(self, width_value):
        """ Setter method for the width attribute"""
        Rectangle.check_int("width", width_value)
        Rectangle.check_positive("width", width_value)

        self.__width = width_value

    @property
    def height(self):
        """ Getter method for the height attribute."""
        return self.__height

    @height.setter
    def height(self, height_value):
        """Setter method for the height attribu"""
        Rectangle.check_int("height", height_value)
        Rectangle.check_positive("height", height_value)
        self.__height = height_value

    @property
    def x(self):
        """Getter method for the x attribute."""
        return self.__x

    @x.setter
    def x(self, x_value):
        """Setter method for the x attribute."""
        Rectangle.check_int("x", x_value)
        Rectangle.check_positive("x", x_value)
        self.__x = x_value

    @property
    def y(self):
        """Getter method for the y attribute."""
        return self.__y

    @y.setter
    def y(self, y_value):
        """Setter method for the y attribute."""
        Rectangle.check_int("y", y_value)
        Rectangle.check_positive("y", y_value)
        self.__y = y_value

    @staticmethod
    def check_int(attr_name, value):
        """ Checks if the value is an integer for the given attribute."""

        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(attr_name))

    @staticmethod
    def check_positive(attr_name, value):
        """ Checks if the value is > 0 for the given attribute."""
        if value <= 0:
            raise ValueError("{} must be > 0".format(attr_name))

    def area(self):
        """calculates the area of the rectangle"""
        return self.__width * self.__height

    def display(self):
        """prints in stdout the Rectangle instance with the character '#' """
        # handling the y axis
        if self.__y > 0:
            for y_axis in range(self.__y):
                print("")

        # handling the X- axis and printing the rec
        for i in range(self.__height):
            for x_axis in range(self.__x):
                print(" ", end="")
            for j in range(self.__width):
                print("#", end="")
            print("")

    def __str__(self):
        """ returns [Rectangle] (<id>) <x>/<y> - <width>/<height>"""
        return ("[Rectangle] ({}) {}/{} - {}/{}").format(
            self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """
        assigns an argument to each attribute order (id, width, height, x, y)
        """
        if args:
            list = [
                'id', '_Rectangle__width', '_Rectangle__height',
                '_Rectangle__x', '_Rectangle__y'
            ]

            for i in range(len(args)):
                if i < len(list):
                    setattr(self, list[i], args[i])

        elif kwargs:
            for key, value in kwargs.items():
                getattr(self, key)
                setattr(self, key, value)

    def to_dictionary(self):
        """returns the dictionary representation of a Rectangle"""
        return {
            'id': self.id,
            'width': self.__width,
            'height': self.__height,
            'x': self.__x,
            'y': self.__y
        }
