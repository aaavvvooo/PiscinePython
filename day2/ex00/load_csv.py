import csv
import numpy as np


def load(path: str) -> list:
    """
    Loads a csv file into a list of numpy arrays.
    path: path to the csv file
    """
    if (not isinstance(path, str)):
        raise TypeError("path must be a string")
    with open(path, 'r') as f:
        reader = csv.reader(f)
        return np.array([row for row in reader])