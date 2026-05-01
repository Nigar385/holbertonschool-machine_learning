#!/usr/bin/env python3
"""Module for calculating the adjugate matrix"""


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
    """Calculates the cofactor matrix"""

    n = len(matrix)

    if n == 1:
        return [[1]]

    cof = []

    for i in range(n):
        cof_row = []
        for j in range(n):
            minor = []
            for r in range(n):
                if r != i:
                    row = matrix[r][:j] + matrix[r][j + 1:]
                    minor.append(row)

            sign = (-1) ** (i + j)
            cof_row.append(sign * determinant(minor))

        cof.append(cof_row)

    return cof


def adjugate(matrix):
    """Calculates the adjugate matrix of a matrix

    Args:
        matrix (list of lists): matrix

    Returns:
        list of lists: adjugate matrix

    Raises:
        TypeError: if matrix is not a list of lists
        ValueError: if matrix is not a non-empty square matrix
    """

    # Validation
    if not isinstance(matrix, list) or matrix == []:
        raise TypeError("matrix must be a list of lists")

    if not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a list of lists")

    n = len(matrix)

    if n == 0 or not all(len(row) == n for row in matrix):
        raise ValueError("matrix must be a non-empty square matrix")

    # Special case
    if n == 1:
        return [[1]]

    cof = cofactor(matrix)

    # Transpose cofactor matrix → adjugate
    adj = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(cof[j][i])
        adj.append(row)

    return adj
