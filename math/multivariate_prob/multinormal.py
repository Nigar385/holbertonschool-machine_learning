#!/usr/bin/env python3
"""Module that defines a Multivariate Normal distribution."""

import numpy as np


class MultiNormal:
    """Represents a Multivariate Normal distribution."""

    def __init__(self, data):
        """Initialize the MultiNormal instance.

        Args:
            data (numpy.ndarray): shape (d, n) containing the data set.

        Raises:
            TypeError: If data is not a 2D numpy.ndarray.
            ValueError: If data contains fewer than 2 data points.
        """
        if not isinstance(data, np.ndarray) or data.ndim != 2:
            raise TypeError("data must be a 2D numpy.ndarray")

        d, n = data.shape

        if n < 2:
            raise ValueError("data must contain multiple data points")

        self.mean = np.mean(data, axis=1, keepdims=True)

        centered = data - self.mean

        self.cov = np.matmul(centered, centered.T) / (n - 1)
