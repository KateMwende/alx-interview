#!/usr/bin/python3
"""
pascal's triangle
"""


def pascal_triangle(n):
    """
    returns a list of lists of integers
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for x in range(1, n):
        row = [1]

        for i in range(1, x):
            row.append(triangle[x - 1][i - 1] + triangle[x - 1][i])
        row.append(1)
        triangle.append(row)
    return triangle
