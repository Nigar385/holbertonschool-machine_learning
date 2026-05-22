#!/usr/bin/env python3
"""Module that removes rows with NaN Close values."""


def prune(df):
    """
    Remove entries where Close contains NaN values.

    Args:
        df: pandas DataFrame.

    Returns:
        Modified pandas DataFrame.
    """
    return df.dropna(subset=["Close"])
