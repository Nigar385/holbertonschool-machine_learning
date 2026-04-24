#!/usr/bin/env python3
"""Module for concatenating 2D matrices along a specific axis."""


def cat_matrices2D(mat1, mat2, axis=0):
    """Concatenate two 2D matrices along a specific axis.

    Args:
        mat1: First 2D matrix containing ints/floats.
        mat2: Second 2D matrix containing ints/floats.
        axis: Axis along which to concatenate (0 for rows, 1 for columns).

    Returns:
        A new concatenated matrix, or None if concatenation is not possible.
    """
    if axis == 0:
        if len(mat1[0]) != len(mat2[0]):
            return None
        return [row[:] for row in mat1] + [row[:] for row in mat2]
    elif axis == 1:
        if len(mat1) != len(mat2):
            return None
        return [mat1[i][:] + mat2[i][:] for i in range(len(mat1))]
    return None
