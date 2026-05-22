#!/usr/bin/env python3
"""Module that converts selected DataFrame values to a NumPy array."""


def array(df):
    """
    Select the last 10 rows of High and Close columns.

    Args:
        df: pandas DataFrame.

    Returns:
        numpy.ndarray of selected values.
    """
    return df[["High", "Close"]].tail(10).to_numpy()
