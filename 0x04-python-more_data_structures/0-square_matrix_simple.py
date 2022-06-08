#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    """computes the square value of all integers of a matrix."""
    return list(map(lambda submat: list(map(lambda e: e**2, submat)), matrix))
