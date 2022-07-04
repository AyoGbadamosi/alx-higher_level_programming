#!/usr/bin/python3
"""
Module for Exact same object task
"""


def is_same_class(obj, a_class):
    """
    Function that returns True if the object is exactly an
    an instance of the specified class otherwise False
    """
    return type(obj) == a_class
