#!/usr/bin/python3
"""Defines a file-appending function."""
def append_write(filename="", text=""):
    """
    Appends a strung to the end of UTF8 file.
    Args:
        filename (str): name of file to append to.
        text (str): the string to append.
        Returns: number of character appended.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
