#!/usr/bin/python3
"""
This module contains only sub class of task
"""


def inherits_from(obj, a_class):
    """Return if the object is an instance of a class that
    inherited from a specified class
    """

    return isinstance(obj, a_class) and type(obj) != a_class
