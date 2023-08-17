#!/usr/bin/python3
"""module documentation"""


def rotate_2d_matrix(matrix):
    """rotate 2d matrix"""
    for index, x in enumerate(zip(*matrix)):
        matrix[index] = list(x)[::-1]
