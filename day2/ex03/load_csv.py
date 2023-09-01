import pandas as pd


def load(path: str) -> list:
    """
    Loads a csv file into a list of numpy arrays.
    path: path to the csv file
    """
    if (not isinstance(path, str)):
        raise TypeError("path must be a string")
    dataset = pd.read_csv(path)
    return dataset
