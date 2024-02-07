#!/usr/bin/python3
"""Defines a text file that does insertion."""


def append_after(filename="", search_string="", new_string=""):
    """creates the text file."""
    text = ""
    with open(filename) as r:
        """open file in read mode."""
        for line in r:
            text.append(line)
            """iterates through the list and appends to text."""
            if search_string in line:
                text.append(new_string + '\n')
                """search string and appends new string after current line."""
    with open(filename, 'w') as w:
        """writes the modified line back to the file."""
        w.writelines(text)
