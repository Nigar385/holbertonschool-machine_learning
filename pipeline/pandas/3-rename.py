#!/usr/bin/env python3
"""Module that renames and formats DataFrame columns."""

import pandas as pd


def rename(df):
    """
    Rename Timestamp column to Datetime and format values.

    Args:
        df: pandas DataFrame containing a Timestamp column.

    Returns:
        Modified pandas DataFrame with only Datetime and Close columns.
    """
    df = df.rename(columns={"Timestamp": "Datetime"})
    df["Datetime"] = pd.to_datetime(df["Datetime"], unit="s")

    return df[["Datetime", "Close"]]
