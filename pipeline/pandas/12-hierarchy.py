#!/usr/bin/env python3
"""Module that creates a hierarchical indexed DataFrame."""

index = __import__('10-index').index


def hierarchy(df1, df2):
    """
    Rearrange MultiIndex and concatenate selected data.

    Args:
        df1: coinbase DataFrame.
        df2: bitstamp DataFrame.

    Returns:
        Concatenated pandas DataFrame.
    """
    df1 = index(df1)
    df2 = index(df2)

    df1 = df1[(df1.index >= 1417411980) &
              (df1.index <= 1417417980)]

    df2 = df2[(df2.index >= 1417411980) &
              (df2.index <= 1417417980)]

    df = __import__('pandas').concat(
        [df2, df1],
        keys=["bitstamp", "coinbase"]
    )

    df = df.swaplevel(0, 1)
    df = df.sort_index()

    return df
