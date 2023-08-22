import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """
    A function takes parameters of 2D array, prints its shape,
    and returns a truncated version of the array.
    param family: 2D array
    param start:  start index
    param end: end index
    """
    if not isinstance(family, list) or any(not isinstance(x, list)
                                           for x in family):
        raise ValueError("family must be a list")
    if not isinstance(start, int) or not isinstance(end, int):
        raise ValueError("start must be an integer")
    print(f"My shape is: {np.array(family).shape}")
    ret_list = np.array(family[start:end])
    print(f"New shape is: {ret_list.shape}")
    return ret_list
