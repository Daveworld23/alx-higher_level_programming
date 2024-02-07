#!/usr/bin/python3
"""Defines a text file that does insertion."""


def append_after(filename="", search_string="", new_string=""):
    """creates the text file."""
    text = []
    with open(filename, 'r') as r:
        """open file in read mode."""
        for line in r:
            text.append(line)
            if search_string in line:
                text.append(new_string)
    with open(filename, 'w') as r:
        w.writeline(text)
