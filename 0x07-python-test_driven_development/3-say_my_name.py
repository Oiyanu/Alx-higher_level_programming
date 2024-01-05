#!/usr/bin/python3
"""say_my_name module"""


def say_my_name(first_name, last_name=""):
    """Prints first and last name.

    Args:
        first_name: first name string
        last_name: last name string

    Raises:
        TypeError: if either @first_name or @last_name is not a string
    """
    if not isinstance(first_name, str) or not first_name:
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {:s} {:s}".format(first_name, last_name))

    if __name__ == "__main__":
        import doctest
        doctest.testfile("tests/3-say_my_name.txt")
