#!/usr/bin/python3
"""
Module for My list task
"""


class MyList(list):
    """
    A class MyList that inherits from list
    """

    def print_sorted(self):
        """Print the list sorted."""
        print(sorted(self))
