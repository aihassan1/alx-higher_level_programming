#!/usr/bin/python3
"""
Module: is_same_class
Description:checks if an object is an instance of a specific class.
"""


def is_same_class(obj, a_class):
    """
    Function: is_same_class
    Checks if an object is an instance of a specific class.
    Args:
        obj: The object to check.
        a_class: The class to compare against.
    Returns:
        True if obj is an instance of a_class, False otherwise.
    """
    return type(obj) == a_class

