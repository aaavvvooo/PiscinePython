import pandas as pd
import os


def load(path: str) -> list:
    """
    Loads a csv file into a list of numpy arrays.
    path: path to the csv file
    """
    if (not isinstance(path, str)):
        raise TypeError("path must be a string")
    if not os.path.exists(path):
        raise FileNotFoundError("path does not exist")
    dataset = pd.read_csv(path)
    return dataset
