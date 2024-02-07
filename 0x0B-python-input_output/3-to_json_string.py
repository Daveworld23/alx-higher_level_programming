#!/usr/bin/python3
"""Defines a string_to_JSON function."""


import json

def to_json_string(my_obj):
    """Returns the JSON relresentation of object"""
    return json.dumps(my_obj)
