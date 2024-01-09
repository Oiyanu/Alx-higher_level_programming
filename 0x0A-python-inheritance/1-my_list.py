#!/usr/bin/python3
"""my_list module"""


class Mylist(list):
    """implements sorted printing for Mylist class"""

    def print_sorted(self):
        """print a list in sorted ascending order"""
        print(sorted(self))
