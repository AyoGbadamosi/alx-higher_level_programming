#!/usr/bin/python3

"""
This module contains My integer task.
"""


class MyInt(int):
    """MyInt class"""

    def __ne__(self, other):
        return super().__eq__(other)

    def __eq__(self, other):
        return super().__ne__(other)
