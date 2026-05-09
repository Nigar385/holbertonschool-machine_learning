#!/usr/bin/env python3
"""
Contains the Poisson class to represent a poisson distribution
"""


class Poisson:
    """
    Class that represents a poisson distribution
    """

    def __init__(self, data=None, lambtha=1.):
        """
        Initialize Poisson distribution
        """
        if data is None:
            if lambtha <= 0:
                raise ValueError("lambtha must be a positive value")
            self.lambtha = float(lambtha)
        else:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain at least multiple values")
            self.lambtha = sum(data) / len(data)

    def pmf(self, k):
        """
        Calculates the value of the PMF for a given number of 'successes'
        """
        k = int(k)
        if k < 0:
            return 0

        e = 2.7182818285
        
        # Factorial of k
        factorial = 1
        for i in range(1, k + 1):
            factorial *= i

        # PMF = (e^-lambda * lambda^k) / k!
        return (e ** (-self.lambtha) * (self.lambtha ** k)) / factorial

    def cdf(self, k):
        """
        Calculates the value of the CDF for a given number of 'successes'
        """
        k = int(k)
        if k < 0:
            return 0

        e = 2.7182818285
        cdf_val = 0
        
        # Sum of PMFs from 0 to k
        for i in range(k + 1):
            # Calculate factorial for each i
            factorial = 1
            for j in range(1, i + 1):
                factorial *= j
            
            # Add PMF of i to total
            cdf_val += (e ** (-self.lambtha) * (self.lambtha ** i)) / factorial
            
        return cdf_val
