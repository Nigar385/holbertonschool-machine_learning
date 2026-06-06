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
    The bins are spaced exactly every 10 units between 0 and 100.
    """
    np.random.seed(5)
    student_grades = np.random.normal(68, 15, 50)
    plt.figure(figsize=(6.4, 4.8))

    # Add labels and title
    plt.xlabel('Grades')
    plt.ylabel('Number of Students')
    plt.title('Project A')

    # Define exact bin boundaries every 10 units from 0 to 100
    bins = range(0, 101, 10)

    # Plot histogram with exact bins and a black outline
    plt.hist(student_grades, bins=bins, edgecolor='black')

    # Set x-axis limit strictly to align with reference layout boundaries
    plt.xlim(0, 100)

    # Display the plot
    plt.show()
