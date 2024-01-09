#!/usr/bin/python3
"""my_list module"""


class Mylist(list):
    """Mylist class"""

    def print_sorted(self):
        """sorts a list of integers in ascending order"""
        print(sorted(self))
