#!/usr/bin/python3
"""
Rotate 2D Matrix
"""


def rotate_2d_matrix(matrix):
    """
    Given an n x n 2D matrix,
    rotate it 90 degrees clockwise
    """
    n = len(matrix)
    # Step 1: Transpose the matrix
    # swapping element at (i, j) with element at (j, i)
    for i in range(n):
        for j in range(i, n):
            temp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = temp

    # Step 2: Reverse each row
    for i in range(n):
        matrix[i].reverse()
