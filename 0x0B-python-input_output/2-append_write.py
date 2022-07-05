#!/usr/bin/python3
"""
This module contains Append to a file task
"""


def append_write(filename="", text=""):
    """function that appends a string at the end of a text file
    and returns the number of characters added
    """
    with open(filename, "a") as f:
        no_of_chars = f.write(text)
    return no_of_chars
