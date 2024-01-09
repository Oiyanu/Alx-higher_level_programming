#!/usr/bin/python3
"""2-is_same_class module"""


def is_same_class(obj, a_class):
    """Determines if an object is exactly an instance of a class

    Args:
        obj: object to be determined
        a_class: type of class
    """
    if type(obj) == a_class:
        return True
    else:
        return False
