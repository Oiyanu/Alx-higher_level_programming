#!/usr/bin/python3
"""Defines a write_file() function"""


def write_file(filename="", text=""):
    """
    writes a string to a text file

    Args:
        filename: name of text file
        text: string to write

    Return:
        number of characters
    """
    with open(filename, "w", encoding="UTF-8") as a_file:
        n_char = a_file.write(text)
    return n_char
