#!/usr/bin/env python3
"""
This module provides a function to plot a histogram of student grades
using matplotlib.
"""
import numpy as np
import matplotlib.pyplot as plt


def frequency():
    """
    Plots a histogram representing the frequency of student grades.
    The bins are spaced every 10 units and bars are outlined in black.
    """
    np.random.seed(5)
    student_grades = np.random.normal(68, 15, 50)
    plt.figure(figsize=(6.4, 4.8))

    # Define bins every 10 units from 0 to 100
    bins = np.arange(0, 101, 10)

    # Plot the histogram with black outlines around the bars
    plt.hist(student_grades, bins=bins, edgecolor='black')

    # Explicitly set x-axis limits and ticks to align perfectly with bins
    plt.xlim(0, 100)
    plt.xticks(bins)

    # Add labels and title
    plt.xlabel('Grades')
    plt.ylabel('Number of Students')
    plt.title('Project A')

    # Display the plot
    plt.show()
