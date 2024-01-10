#!/usr/bin/python3
"""Defines from_json_string() function"""
import json


def from_json_string(my_str):
    """
    Deserializes json string to python object

    Args:
        my_str: object to be deserialized

    Return:
        python object
    """
    p_obj = json.loads(my_str)
    return p_obj
