#!/usr/bin/env python3
"""Module that sets the Timestamp column as index."""


def index(df):
    """
    Set the Timestamp column as the DataFrame index.

    Args:
        df: pandas DataFrame.

    Returns:
        Modified pandas DataFrame.
    """
    return df.set_index("Timestamp")
