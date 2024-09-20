import pandas as pd


def load_data(filename):
    """load in your data"""
    data = pd.read_csv(filename)
    return data
