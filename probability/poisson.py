#!/usr/bin/env python3
"""
Poisson distribution class
"""

class Poisson:
    """
    Represents a Poisson distribution
    """

    def __init__(self, data=None, lambtha=1.):
        """
        data: list of observed data
        lambtha: expected number of occurrences
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
            mean = sum(data) / len(data)
            self.lambtha = mean

    def pmf(self, k):
        """
        Calculates the value of the PMF for a given number of successes.
        """
        if k < 0:
            return 0

        k = int(k)
        e = 2.7182818285
        factorial = 1
        for i in range(1, k + 1):
            factorial *= i
        pmf = (self.lambtha ** k) * (e ** (-self.lambtha)) / factorial
        return pmf

    def cdf(self, k):
        """
        Calculates the cumulative distribution function (CDF)
        for a given number of successes.
        """
        if k < 0:
            return 0

        k = int(k)
        e = 2.7182818285

        # CDF is the sum of PMFs from 0 to k
        cdf = 0
        for i in range(0, k + 1):
            factorial = 1
            for j in range(1, i + 1):
                factorial *= j
            cdf += (self.lambtha ** i) * (e ** (-self.lambtha)) / factorial
        return cdf
