#!/usr/bin/env python3
"""Module that calculates a correlation matrix."""

import numpy as np


def correlation(C):
    """Calculates a correlation matrix.

    Args:
        C (numpy.ndarray): shape (d, d) containing a covariance matrix.

    Returns:
        numpy.ndarray: correlation matrix.

    Raises:
        TypeError: If C is not a numpy.ndarray.
        ValueError: If C is not a 2D square matrix.
    """
    if not isinstance(C, np.ndarray):
        raise TypeError("C must be a numpy.ndarray")

    if C.ndim != 2 or C.shape[0] != C.shape[1]:
        raise ValueError("C must be a 2D square matrix")

    stddev = np.sqrt(np.diag(C))

    corr = C / np.outer(stddev, stddev)

    return corr
