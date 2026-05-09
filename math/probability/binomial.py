#!/usr/bin/env python3
"""
Contains the Binomial class to represent a binomial distribution
"""


class Binomial:
    """
    Class that represents a binomial distribution
    """

    def __init__(self, data=None, n=1, p=0.5):
        """
        Initialize Binomial distribution
        """
        if data is None:
            if n <= 0:
                raise ValueError("n must be a positive value")
            if p <= 0 or p >= 1:
                raise ValueError("p must be greater than 0 and less than 1")
            self.n = int(n)
            self.p = float(p)
        else:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")

            # Mean (mu) = sum(x) / len(data)
            mean = sum(data) / len(data)

            # Variance (sigma^2) = sum((x - mean)^2) / len(data)
            sum_sq_diff = 0
            for x in data:
                sum_sq_diff += (x - mean) ** 2
            variance = sum_sq_diff / len(data)

            # p = 1 - (variance / mean)
            # n = mean / p
            p_initial = 1 - (variance / mean)
            n_estimated = mean / p_initial

            # Round n to nearest integer
            self.n = int(round(n_estimated))

            # Recalculate p based on rounded n
            self.p = float(mean / self.n)
