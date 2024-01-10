#!/usr/bin/python3
"""Defines a append_write() function"""


def append_write(filename="", text=""):
    """
    Appends a string to end a text file

    Args:
        filename: name of text file
        text: string to append

    Return:
        number of characters appended
    """
    with open(filename, "a", encoding="UTF-8") as a_file:
        n_char = a_file.write(text)
    return n_char
