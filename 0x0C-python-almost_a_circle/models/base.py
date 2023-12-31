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

        if list_objs is None:
            list_objs = []

        filename = cls.__name__ + '.json'

        with open(filename, 'w') as file:
            list_dicts = [o.to_dictionary() for o in list_objs]
            file.write(cls.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """ returns the list of the JSON string representation json_string"""
        if json_string is None:
            return []

        return (json.loads(json_string))

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            dummy_instance = cls(5, 6)

        elif cls.__name__ == 'Square':
            dummy_instance = cls(5)

        dummy_instance.update(**dictionary)

        return dummy_instance

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        filename = cls.__name__ + ".json"
        try:
            with open(filename, 'r') as file:
                content = file.read()
                list = cls.from_json_string(content)
                list_instances = []
                for element in list:
                    instance = cls.create(**element)
                    list_instances.append(instance)

                return list_instances

        except FileNotFoundError:
            return []
