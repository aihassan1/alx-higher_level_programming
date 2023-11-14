#!/usr/bin/python3
"""this is the module doc"""
from models.rectangle import Rectangle


class Square(Rectangle):

    def __init__(self, size, x=0, y=0, id=None):
        """class constructor"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ returns [Square] (<id>) <x>/<y> - <width>/<height>"""
        return ("[Square] ({}) {}/{} - {}").format(self.id, self.x, self.y,
                                                   self.width)

    @property
    def size(self):
        """size getter"""
        return self.height

    @size.setter
    def size(self, value):
        """size setter"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute order (id, size, x, y)"""
        list = ['id', 'size', 'x', 'y']

        if args:
            for i in range(len(args)):
                setattr(self, list[i], args[i])

        elif kwargs:
            for key, value in kwargs.items():
                getattr(self, key)
                setattr(self, key, value)