#!/usr/bin/python3
"""
Module to check inheritance.
"""


def inherits_from(obj, a_class):
    """
    Function to check if an object inherits from a specific class.
    Args:
        obj: The object to check.
        a_class: The class to check against.
    Returns:
        True if the object inherits from the class, False otherwise.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return issubclass(type(obj), a_class)
    else:
        return False
