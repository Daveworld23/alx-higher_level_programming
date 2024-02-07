#!/usr/bin/python3
"""Defines a class to JSON function."""


def class_to_json(obj):
    """Returns the dictionary representation of the data."""
    return obj.__dict__
