#!/usr/bin/python3

"""
This module contains Can I? task
"""


def add_attribute(obj, key, value):
    """new attr to an object"""
    if not hasattr(obj, "__slots__") and not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    if hasattr(obj, "__slots__") and not hasattr(obj, key):
        raise TypeError("can't add new attribute")
    setattr(obj, key, value)
