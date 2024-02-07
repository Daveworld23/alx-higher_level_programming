#!/usr/bin/python3
"""Add arguments to a list and save them to a file."""


import sys


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

old = list(sys.argv[1:])

try:
    new = load_from_json_file("add_item.json")
except FileNotFoundError:
    new = []
new.extend(old)
save_to_json_file(new, "add_item.json")
