#!/usr/bin/python3
"""Defines save_to_json_file() function"""
import json


def save_to_json_file(my_obj, filename):
    """
    serializes the object and saves to file

    Args:
        my_obj: object to be serialized
        filename: file to where JSON string rep is to be written
    """
    with open(filename, 'w', encoding="UTF-8") as j_file:
        json.dump(my_obj, j_file)
