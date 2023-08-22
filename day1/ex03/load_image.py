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
        print(f"The shape of image is: {rgb_array.shape}")
        print(rgb_array[0])
        return rgb_array
    except Exception as e:
        print(f"Error: {e}")
        exit(1)
