#!/usr/bin/env python3
"""Module that creates a pandas DataFrame from a NumPy array."""

import pandas as pd


def from_numpy(array):
    """
    Create a pandas DataFrame from a NumPy array.

    Args:
        array: numpy.ndarray to convert into a DataFrame.

    Returns:
        A pandas DataFrame with alphabetically capitalized column labels.
    """
    columns = [chr(65 + i) for i in range(array.shape[1])]
    return pd.DataFrame(array, columns=columns)
