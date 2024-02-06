#!/usr/bin/python3
"""Defines a JSON_to_string object."""
def from_json_string(my_str):
    """Returns the object representation of a JSON string."""
    return json.loads(my_str)
