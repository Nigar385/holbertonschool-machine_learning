#!/usr/bin/env python3
"""
Contains the Exponential class to represent an exponential distribution
"""


class Exponential:
    """
    Class that represents an exponential distribution
    """

    def __init__(self, data=None, lambtha=1.):
        """
        Initialize Exponential distribution
        Args:
            data (list): list of the data to be used to estimate
                the distribution
            lambtha (float): expected number of occurrences in a
                given timeframe
        """
        if data is None:
            if lambtha <= 0:
                raise ValueError("lambtha must be a positive value")
            self.lambtha = float(lambtha)
        else:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            # For Exponential distribution, lambtha = 1 / mean
            self.lambtha = 1 / (sum(data) / len(data))
