import numpy as np


def give_bmi(height: list[int | float], weight: list[int | float]) \
        -> list[int | float]:
    """
    Calculates BMI from height and weight
    :param height: list of heights
    :param weight: list of weights
    :return: list of BMI
    """
    height = np.array(height)
    weight = np.array(weight)
    if len(height) != len(weight):
        raise ValueError("height and weight must have the same length")
    if any(not isinstance(x, (int, float)) for x in height)\
            or any(not isinstance(x, (int, float)) for x in weight):
        raise ValueError("height and weight must be numbers")
    if any(x <= 0 for x in height) or any(x <= 0 for x in weight):
        raise ValueError("height and weight must be positive")
    return list(np.array(weight) / np.array(height) ** 2)


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    Applies a limit to BMI
    :param bmi: list of BMI
    :param limit: limit
    :return: list of booleans
    """
    if not isinstance(limit, int):
        raise ValueError("limit must be an integer")
    if limit <= 0:
        raise ValueError("limit must be positive")
    return list(np.array(bmi) > limit)
