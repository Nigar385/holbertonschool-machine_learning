#!/usr/bin/env python3
"""Module that converts selected DataFrame values to a NumPy array."""

import pandas as pd


def array(df):
    """
    Select the last 10 rows of High and Close columns as a NumPy array.

    Args:
        df: pandas DataFrame containing High and Close columns.

    Returns:
        A NumPy ndarray containing the selected values.
    """
    return df[["High", "Close"]].tail(10).to_numpy()
