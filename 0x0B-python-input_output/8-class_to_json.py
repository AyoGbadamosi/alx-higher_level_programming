#!/usr/bin/python3
"""
This module contains Class to JSON task
"""


def class_to_json(obj):
    """Returns dictionary description with simple data structure"""
    return obj.__dict__
