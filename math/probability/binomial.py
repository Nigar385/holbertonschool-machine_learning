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

            mean = sum(data) / len(data)
            sum_sq_diff = 0
            for x in data:
                sum_sq_diff += (x - mean) ** 2
            variance = sum_sq_diff / len(data)

            p_initial = 1 - (variance / mean)
            n_estimated = mean / p_initial
            self.n = int(round(n_estimated))
            self.p = float(mean / self.n)

    def pmf(self, k):
        """
        Calculates the value of the PMF for a given number of successes
        """
        k = int(k)
        if k < 0 or k > self.n:
            return 0

        def factorial(num):
            """ Manual factorial calculation """
            res = 1
            for i in range(1, num + 1):
                res *= i
            return res

        n_f = factorial(self.n)
        k_f = factorial(k)
        nk_f = factorial(self.n - k)

        n_cr = n_f / (k_f * nk_f)
        return n_cr * (self.p ** k) * ((1 - self.p) ** (self.n - k))

    def cdf(self, k):
        """
        Calculates the value of the CDF for a given number of successes
        """
        k = int(k)
        if k < 0:
            return 0

        cdf_val = 0
        for i in range(k + 1):
            cdf_val += self.pmf(i)

        return cdf_val
