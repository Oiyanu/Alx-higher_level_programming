#!/usr/bin/python3
"""Module for inherits_from method"""


def inherits_from(obj, a_class):
    """Determines if an object is a true subclass of a class

    Args:
        obj: object to be checked
        a_class: type of class
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    else:
        return False
