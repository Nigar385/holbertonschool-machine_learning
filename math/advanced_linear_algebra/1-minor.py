#!/usr/bin/env python3
"""Module that calculates the minor matrix of a matrix."""


def determinant(matrix):
    """Calculate the determinant of a matrix."""

    if matrix == [[]]:
        return 1

    if len(matrix) == 1:
        return matrix[0][0]

    if len(matrix) == 2:
        return ((matrix[0][0] * matrix[1][1]) -
                (matrix[0][1] * matrix[1][0]))

    det = 0

    for col in range(len(matrix)):
        submatrix = []

        for row in range(1, len(matrix)):
            new_row = matrix[row][:col] + matrix[row][col + 1:]
            submatrix.append(new_row)

        det += ((-1) ** col) * matrix[0][col] * determinant(submatrix)

    return det


def minor(matrix):
    """Calculate the minor matrix of a matrix."""

    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix)):
        raise TypeError("matrix must be a list of lists")

    n = len(matrix)

    if any(len(row) != n for row in matrix):
        raise ValueError("matrix must be a non-empty square matrix")

    if matrix == [[]]:
        raise ValueError("matrix must be a non-empty square matrix")

    if n == 1:
        return [[1]]

    minor_matrix = []

    for i in range(n):
        row = []

        for j in range(n):
            submatrix = []

            for r in range(n):
                if r != i:
                    new_row = []

                    for c in range(n):
                        if c != j:
                            new_row.append(matrix[r][c])

                    submatrix.append(new_row)

            row.append(determinant(submatrix))

        minor_matrix.append(row)

    return minor_matrix
