#!/usr/bin/python3
"""
This module contains Pascal's Triangle task
"""


def pascal_triangle(n):
    """function that returns a list of integers representing the
    Pascal's triangle of n
    """

    triangle = []
    if n <= 0:
        return triangle

    triangle = [[1]]
    for i in range(n - 1):
        line = triangle[-1]
        tri = [1]
        for i in range(len(line) - 1):
            tri.append(line[i] + line[i + 1])
        tri.append(1)
        triangle.append(tri)
    return triangle
