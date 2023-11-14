#!/usr/bin/python3
"""Module for the Square class."""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Represents a square, inherits from Rectangle."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a Square instance."""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Return a string representation of the Square."""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)

    @property
    def size(self):
        """Getter method for the size attribute."""
        return self.width

    @size.setter
    def size(self, value):
        """Setter method for the size attribute."""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Assigns arguments to each attribute in order (id, size, x, y)."""
        attribute_list = ['id', 'size', 'x', 'y']

        if args:
            for i in range(len(args)):
                setattr(self, attribute_list[i], args[i])

        elif kwargs:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)
