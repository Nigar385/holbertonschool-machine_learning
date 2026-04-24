#!/usr/bin/env python3
"""Module that defines np_elementwise function"""


def np_elementwise(mat1, mat2):
    """Performs element-wise operations on numpy arrays"""
    return (mat1 + mat2, mat1 - mat2, mat1 * mat2, mat1 / mat2)
