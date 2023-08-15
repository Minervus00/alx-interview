#!/usr/bin/python3
"""Rotate a 2D Matrix in python"""


def transpose(matrix):
    """Transposes the given matrix in place"""
    for i in range(len(matrix)):
        for j in range(i+1, len(matrix)):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


def rotate_2d_matrix(matrix):
    """Rotates the given matrix in place clockwise"""
    transpose(matrix)
    # reverse each row
    for row in matrix:
        row.reverse()
