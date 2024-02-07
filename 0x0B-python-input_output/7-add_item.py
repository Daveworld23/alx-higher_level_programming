#!/usr/bin/python3
"""Add arguments to a list and save them to a file."""


import sys


if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = \
            __import__('6-load_from_json_file').load_from_json_file

    try:
        new = load_from_json_file("add_item.json")
    except FileNotFoundError:
        new = []
        """if the file doesn't exist, load empty file"""
    new.extend(sys.argv[1:])
    """extend the list and save the file afterwards"""
    save_to_json_file(new, "add_item.json")
