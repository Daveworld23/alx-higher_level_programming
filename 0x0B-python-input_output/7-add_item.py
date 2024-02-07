#!/usr/bin/python3
"""Add arguments to a list and save them to a file."""


import sys


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

items = list(sys.argv[1:])

try:
    item = load_from_json_file('add_item.json')
except Exception:
    item = []

    item.extend(items)
    save_to_json_file(item, 'add_item.json')
