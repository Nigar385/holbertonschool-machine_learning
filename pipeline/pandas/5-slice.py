#!/usr/bin/env python3
"""Module that slices specific columns and rows from a DataFrame."""

import pandas as pd


def slice(df):
    """
    Extract specific columns and select every 60th row.

    Args:
        df: pandas DataFrame.

    Returns:
        A sliced pandas DataFrame.
    """
    return df[["High", "Low", "Close", "Volume_(BTC)"]][::60]
