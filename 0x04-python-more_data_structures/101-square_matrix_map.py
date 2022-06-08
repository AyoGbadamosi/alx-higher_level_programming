#!/usr/bin/python3

def square_matrix_map(matrix=[]):
    """computes the square value of all integers of a matrix using map"""
    return list(map(lambda submat: list(map(lambda e: e**2, submat)), matrix))
