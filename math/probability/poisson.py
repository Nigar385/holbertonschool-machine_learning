#!/usr/bin/env python3
"""Poisson distribution module"""


class Poisson:
    """Represents a Poisson distribution"""

    e = 2.7182818285

    def __init__(self, data=None, lambtha=1.):
        """Initialize Poisson distribution"""
        if data is None:
            if lambtha <= 0:
                raise ValueError("lambtha must be a positive value")
            self.lambtha = float(lambtha)
        else:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            self.lambtha = float(sum(data) / len(data))

    def factorial(self, n):
        """Calculates factorial of n"""
        fact = 1
        for i in range(1, n + 1):
            fact *= i
        return fact

    def pmf(self, k):
        """Calculates PMF for a given k"""
        if not isinstance(k, int):
            k = int(k)

        if k < 0:
            return 0

        return ((self.e ** (-self.lambtha)) *
                (self.lambtha ** k) /
                self.factorial(k))
