#!/usr/bin/env python3
"""
This module provides a function to plot a simple line graph using matplotlib.
"""
import numpy as np
import matplotlib.pyplot as plt


def line():
    """
    Plots y as a solid red line where y = x^3 for x in the range [0, 10].
    The x-axis limits are explicitly set to range from 0 to 10.
    """
    y = np.arange(0, 11) ** 3
    plt.figure(figsize=(6.4, 4.8))

    # Generate x values corresponding to y indices (0 to 10)
    x = np.arange(0, 11)

    # Plot y as a solid red line ('r-')
    plt.plot(x, y, 'r-')

    # Set the x-axis limits from 0 to 10
    plt.xlim(0, 10)

    # Display the plot
    plt.show()
