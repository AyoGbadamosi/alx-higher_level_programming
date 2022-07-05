#!/usr/bin/python3
"""
This module contains create object from a JSON file task
"""


import json


def load_from_json_file(filename):
    """function that creates an Object from a JSON file"""
    with open(filename, "r") as f:
        return json.load(f)
