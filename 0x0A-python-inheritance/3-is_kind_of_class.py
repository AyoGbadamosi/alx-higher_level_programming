#!/usr/bin/phython3
"""
This module contains same class
or inherit from task
"""


def is_kind_of_class(obj, a_class):
    """
    Return True if the object is an instance of, or if the object
    is an instance of a class that it inherits from otherwise False
    """
    return isinstance(obj, a_class)
