#!/usr/bin/env python3
"""Module that concatenates two DataFrames."""

index = __import__('10-index').index


def concat(df1, df2):
    """
    Concatenate two DataFrames with keys.

    Args:
        df1: coinbase DataFrame.
        df2: bitstamp DataFrame.

    Returns:
        Concatenated pandas DataFrame.
    """
    df1 = index(df1)
    df2 = index(df2)

    df2 = df2[df2.index <= 1417411920]

    return __import__('pandas').concat(
        [df2, df1],
        keys=["bitstamp", "coinbase"]
    )
