#!/usr/bin/env python3
"""
This module provides a function to plot a stacked bar graph of fruit
quantities per person using matplotlib.
"""
import numpy as np
import matplotlib.pyplot as plt


def bars():
    """
    Plots a stacked bar graph representing fruit quantities for three people.
    The fruits are stacked in a specific sequence with specific colors and a
    y-axis range from 0 to 80.
    """
    np.random.seed(5)
    fruit = np.random.randint(0, 20, (4, 3))
    plt.figure(figsize=(6.4, 4.8))

    people = ['Farrah', 'Fred', 'Felicia']
    fruits = ['apples', 'bananas', 'oranges', 'peaches']
    colors = ['red', 'yellow', '#ff8000', '#ffe5b4']
    width = 0.5

    # Initialize the bottom values array for stacking to 0
    bottom = np.zeros(len(people))

    # Loop through rows of fruit to stack them sequentially from bottom to top
    for i in range(len(fruits)):
        plt.bar(people, fruit[i], width=width, bottom=bottom,
                color=colors[i], label=fruits[i])
        # Accumulate the current row's heights for the next layer's base
        bottom += fruit[i]

    # Set axes styling and ranges
    plt.ylabel('Quantity of Fruit')
    plt.ylim(0, 80)
    plt.yticks(np.arange(0, 81, 10))
    plt.title('Number of Fruit per Person')

    # Add the legend to identify the fruit colors
    plt.legend()

    # Display the plot
    plt.show()
