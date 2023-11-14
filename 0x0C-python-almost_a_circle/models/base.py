#!/usr/bin/python3
"""this define the module for creating the base class"""


class Base:
    """Defines a base class for objects."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes the base class."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
