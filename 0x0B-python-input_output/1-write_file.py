#!/usr/bin/python3
"""Defines a function that writes to file."""
def write_file(filename="", text=""):
    """
    Writes string to UTF8 file.
    Args:
        filename (str): name of file
        text (str): text to write
    Returns:
        Number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
