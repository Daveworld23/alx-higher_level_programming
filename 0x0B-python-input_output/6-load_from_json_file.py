#!/usr/bin/python3
"""Defines a file-reading JSON function."""
import json
def load_from_json_file(filename):
    """Create an ovject from JSON file."""
    with open(filename) as f:
        return json.load(f)
