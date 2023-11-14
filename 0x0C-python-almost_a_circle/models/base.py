#!/usr/bin/python3
"""this define the module for creating the base class"""

import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None:
            return ("[]")
        json_string = json.dumps(list_dictionaries)
        return json_string

    @classmethod
    def save_to_file(cls, list_objs):
        """ writes the JSON string representation of list_objs to a file"""
        file_name = ("{}.json".format(cls))
        with open(file_name, 'w'):
            cls.to_json_string(list_objs)
