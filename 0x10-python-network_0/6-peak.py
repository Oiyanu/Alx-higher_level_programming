#!/usr/bin/python3
"""Find a peak"""


def find_peak(list_of_integers):
    """Finds a peak function."""
    if list_of_integers:
        list_of_integers.sort(reverse=True)
        return list_of_integers[0]
