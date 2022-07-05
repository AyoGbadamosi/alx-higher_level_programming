#!/usr/bin/python3
"""
This module contains Write to a file task
"""


def write_file(filename="", text=""):
    """function that writes a string to a text file
    and returns the number of characters written
    """
    with open(filename, "w", encoding="utf-8") as f:
        f.write(text)
        no_of_chars = f.tell()
    return no_of_chars
