#!/usr/bin/python3
"""
This module contains Student to JSON task
"""


class Student:
    """Student class"""

    def __init__(self, first_name, last_name, age):
        """class Initialization"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Return Dictionary to JSON"""
        return self.__dict__
