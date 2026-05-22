#!/usr/bin/env python3
"""Module that sorts a DataFrame by High price."""


def high(df):
    """
    Sort the DataFrame by the High column in descending order.

    Args:
        df: pandas DataFrame.

    Returns:
        Sorted pandas DataFrame.
    """
    return df.sort_values(by="High", ascending=False)
