#!/usr/bin/env python3
"""Module for calculating the determinant of a matrix"""


def determinant(matrix):
    """Calculates the determinant of a matrix

    Args:
        matrix (list of lists): matrix to calculate determinant of

    Returns:
        determinant of the matrix

    Raises:
        TypeError: if matrix is not a list of lists
        ValueError: if matrix is not a square matrix
    """

    # Check if matrix is a list of lists
    if not isinstance(matrix, list) or matrix == []:
        raise TypeError("matrix must be a list of lists")

    if not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a list of lists")

    # Special case: [[]] -> 0x0 matrix
    if matrix == [[]]:
        return 1

    n = len(matrix)

    # Check square matrix
    if not all(len(row) == n for row in matrix):
        raise ValueError("matrix must be a square matrix")

    # Base cases
    if n == 1:
        return matrix[0][0]

    if n == 2:
        return (matrix[0][0] * matrix[1][1] -
                matrix[0][1] * matrix[1][0])

    # Recursive determinant (Laplace expansion)
    det = 0
    for col in range(n):
        # Build submatrix
        submatrix = []
        for row in matrix[1:]:
            sub_row = row[:col] + row[col + 1:]
            submatrix.append(sub_row)

        # Cofactor expansion
        sign = (-1) ** col
        det += sign * matrix[0][col] * determinant(submatrix)

    return det
