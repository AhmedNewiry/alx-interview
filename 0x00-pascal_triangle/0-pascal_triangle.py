#!/usr/bin/python3
"""
This module contains a function to generate Pascal's Triangle.
"""


def pascal_triangle(n):
    """
    Generate Pascal's Triangle up to the n-th row.

    Args:
        n (int): The number of rows of Pascal's Triangle to generate.

    Returns:
        list of list of int: Pascal's Triangle up to the n-th row.
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        row.append(1)
        triangle.append(row)

    return triangle
