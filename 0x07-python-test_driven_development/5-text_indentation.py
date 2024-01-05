#!/usr/bin/python3
"""text_indentation module"""


def text_indentation(text):
    """Method for adding two new lines after '.?:' chars.

    Args:
        text: The str text.

    Raise:
        TypeError: If text is not a str.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for delim in ".?:":

        text = (delim + "\n\n").join(
            [line.strip(" ") for line in text.split(delim)])

    print(text, end="")


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/5-text_indentation.txt")
