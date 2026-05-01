#!/usr/bin/env python3
"""Module that calculates the cofactor matrix of a matrix."""


def determinant(matrix):
    """Recursively calculates determinant of a square matrix."""

    if matrix == [[]]:
        return 1

    if len(matrix) == 1:
        return matrix[0][0]

    if len(matrix) == 2:
        return (matrix[0][0] * matrix[1][1]) - (matrix[0][1] * matrix[1][0])

    det = 0
    for col in range(len(matrix)):
        submatrix = []

        for row in range(1, len(matrix)):
            new_row = matrix[row][:col] + matrix[row][col + 1:]
            submatrix.append(new_row)

        det += ((-1) ** col) * matrix[0][col] * determinant(submatrix)

    return det


def minor(matrix):
    """Returns minor matrix of a square matrix."""

    n = len(matrix)
    result = []

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
        result.append(row)

    return result


def cofactor(matrix):
    """Calculates the cofactor matrix of a matrix."""

    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix)):
        raise TypeError("matrix must be a list of lists")

    n = len(matrix)

    if any(len(row) != n for row in matrix):
        raise ValueError("matrix must be a non-empty square matrix")

    if matrix == [[]]:
        raise ValueError("matrix must be a non-empty square matrix")

    minors = minor(matrix)

    cofactor_matrix = []

    for i in range(n):
        row = []
        for j in range(n):
            sign = (-1) ** (i + j)
            row.append(sign * minors[i][j])
        cofactor_matrix.append(row)

    return cofactor_matrix
