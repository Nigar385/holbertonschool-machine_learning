#!/usr/bin/env python3
"""Module for calculating the cofactor matrix"""


def determinant(matrix):
    """Calculates the determinant of a matrix"""

    if matrix == [[]]:
        return 1

    n = len(matrix)

    if n == 1:
        return matrix[0][0]

    if n == 2:
        return (matrix[0][0] * matrix[1][1] -
                matrix[0][1] * matrix[1][0])

    det = 0
    for col in range(n):
        submatrix = []
        for row in matrix[1:]:
            submatrix.append(row[:col] + row[col + 1:])

        sign = (-1) ** col
        det += sign * matrix[0][col] * determinant(submatrix)

    return det


def cofactor(matrix):
    """Calculates the cofactor matrix of a matrix

    Args:
        matrix (list of lists): matrix to calculate cofactors of

    Returns:
        list of lists: cofactor matrix

    Raises:
        TypeError: if matrix is not a list of lists
        ValueError: if matrix is not a non-empty square matrix
    """

    # Validate input
    if not isinstance(matrix, list) or matrix == []:
        raise TypeError("matrix must be a list of lists")

    if not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a list of lists")

    n = len(matrix)

    if n == 0 or not all(len(row) == n for row in matrix):
        raise ValueError("matrix must be a non-empty square matrix")

    # Special case: 1x1 matrix
    if n == 1:
        return [[1]]

    cof = []

    for i in range(n):
        cof_row = []
        for j in range(n):
            # Build minor matrix
            minor = []
            for r in range(n):
                if r != i:
                    row = matrix[r][:j] + matrix[r][j + 1:]
                    minor.append(row)

            # Cofactor formula
            sign = (-1) ** (i + j)
            cof_value = sign * determinant(minor)
            cof_row.append(cof_value)

        cof.append(cof_row)

    return cof
