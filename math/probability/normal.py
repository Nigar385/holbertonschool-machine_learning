#!/usr/bin/env python3
"""
Contains the Normal class to represent a normal distribution
"""


class Normal:
    """
    Class that represents a normal distribution
    """

    def __init__(self, data=None, mean=0., stddev=1.):
        """
        Initialize Normal distribution
        Args:
            data (list): list of the data to be used to estimate
            mean (float): mean of the distribution
            stddev (float): standard deviation of the distribution
        """
        if data is None:
            if stddev <= 0:
                raise ValueError("stddev must be a positive value")
            self.mean = float(mean)
            self.stddev = float(stddev)
        else:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")

            # Calculate mean: sum(x) / n
            self.mean = float(sum(data) / len(data))

            # Calculate variance: sum((x - mean)^2) / n
            sum_sq_diff = 0
            for x in data:
                sum_sq_diff += (x - self.mean) ** 2
            variance = sum_sq_diff / len(data)

            # Standard deviation: square root of variance
            self.stddev = variance ** 0.5
