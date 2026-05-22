#!/usr/bin/env python3
"""Module that loads data from a file into a pandas DataFrame."""

import pandas as pd


def from_file(filename, delimiter):
    """
    Load data from a file as a pandas DataFrame.

    Args:
        filename: The file to load from.
        delimiter: The column separator.

    Returns:
        The loaded pandas DataFrame.
    """
    return pd.read_csv(filename, sep=delimiter)
