#!/usr/bin/python3
"""
0-rotate_2d_matrix.py
This module contains a function that
rotates an n x n 2D matrix 90 degrees
clockwise in-place.
"""


def rotate_2d_matrix(matrix):
    """
    Rotates an n x n 2D matrix 90 degrees clockwise in-place.

    Args:
        matrix (list of list of int): 2D matrix to rotate.

    The rotation is achieved by first transposing the matrix and then
    reversing each row to complete the 90-degree clockwise rotation.
    """
    # Step 1: Transpose the matrix
    n = len(matrix)
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Step 2: Reverse each row
    for i in range(n):
        matrix[i].reverse()
