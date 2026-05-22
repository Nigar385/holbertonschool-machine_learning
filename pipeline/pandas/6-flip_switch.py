#!/usr/bin/env python3
"""Module that flips and transposes a DataFrame."""


def flip_switch(df):
    """
    Sort the DataFrame in reverse chronological order
    and transpose it.

    Args:
        df: pandas DataFrame.

    Returns:
        Transformed pandas DataFrame.
    """
    return df.iloc[::-1].transpose()
