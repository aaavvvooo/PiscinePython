import numpy as np
from PIL import Image


def ft_load(path: str) -> list[int]:
    """
    A function that takes a path to an image and returns a list of its RGB
    values
    param path: path to image
    """
    try:
        image = Image.open(path)
        rgb_array = np.array(image)
        return rgb_array
    except Exception as e:
        print(f"Error3: {e}")
        exit(1)
