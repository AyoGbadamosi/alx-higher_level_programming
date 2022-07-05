#!/usr/bin/python3
"""
This module contains Read file task
"""


def read_file(filename=""):
    """reads a text file (UTF8) and prints it to stdout"""
    with open(filename, "r", encoding="utf-8") as f:
        contents = f.read()
    print(contents, end="")
