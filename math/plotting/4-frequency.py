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
    The histogram splits data into 10 bins with black edge outlines.
    """
    np.random.seed(5)
    student_grades = np.random.normal(68, 15, 50)
    plt.figure(figsize=(6.4, 4.8))

    # Plot histogram with 10 bins and black outlines
    plt.hist(student_grades, bins=10, edgecolor='black')

    # Add labels and title
    plt.xlabel('Grades')
    plt.ylabel('Number of Students')
    plt.title('Project A')

    # Display the plot
    plt.show()
