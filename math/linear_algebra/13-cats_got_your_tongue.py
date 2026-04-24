#!/usr/bin/env python3
"""Module that defines np_cat function"""

import numpy as np


def np_cat(mat1, mat2, axis=0):
    """Concatenates two numpy arrays along a specific axis"""
    return np.concatenate((mat1, mat2), axis=axis)
