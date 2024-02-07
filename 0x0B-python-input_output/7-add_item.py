#!/usr/bin/python3
"""Add arguments to a list and save them to a file."""


import sys


from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file

old = list(sys.argv[1:])

try:
    new = load_from_json_file('add_item.json')
except FileNotFoundError:
    new = []
new.extend(old)
save_to_json_file(new, 'add_item.json')
