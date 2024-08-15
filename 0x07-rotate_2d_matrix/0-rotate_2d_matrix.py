#!/usr/bin/python3
"""Rotation of two-dimensional array in place
"""


def rotate_2d_matrix(matrix):
    """Rotating a two-dimensional array[matrix] 90 degrees clockwise in place.
    """
    n = len(matrix)
    # Transpose the matrix
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    # Reverse each row
    for i in range(n):
        matrix[i].reverse()
