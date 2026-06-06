#!/usr/bin/env python3
"""
This module provides a function to plot two exponential decay curves
simultaneously, representing C-14 and Ra-226.
"""
import numpy as np
import matplotlib.pyplot as plt


def two():
    """
    Plots two radioactive decay curves with different line styles and colors,
    including axes limits, specific labels, and an upper-right legend.
    """
    x = np.arange(0, 21000, 1000)
    r = np.log(0.5)
    t1 = 5730
    t2 = 1600
    y1 = np.exp((r / t1) * x)
    y2 = np.exp((r / t2) * x)
    plt.figure(figsize=(6.4, 4.8))

    # Plot y1 as a dashed red line and y2 as a solid green line
    plt.plot(x, y1, 'r--', label='C-14')
    plt.plot(x, y2, 'g-', label='Ra-226')

    # Set the x and y axis ranges
    plt.xlim(0, 20000)
    plt.ylim(0, 1)

    # Add labels and title
    plt.xlabel('Time (years)')
    plt.ylabel('Fraction Remaining')
    plt.title('Exponential Decay of Radioactive Elements')

    # Add legend to the upper right corner
    plt.legend(loc='upper right')

    # Display the plot
    plt.show()
