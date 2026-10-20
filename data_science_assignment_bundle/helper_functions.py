"""Reusable helper functions for the sample movie ratings project."""
import pandas as pd


def load_ratings(file_path):
    """Load a processed movie ratings CSV file."""
    return pd.read_csv(file_path)


def average_rating(df, rating_column="rating"):
    """Return the average value of the selected rating column."""
    return df[rating_column].mean()
