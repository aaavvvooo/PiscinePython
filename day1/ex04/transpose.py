from load_image import ft_load
from matplotlib import pyplot as plt
import numpy as np


def zoom(path: str) -> list[int]:
    """
    Takes a path to image and zooms it
    """
    try:
        image = ft_load(path)
        sliced_image = image[100:500, 450:850]
        sliced_image = sliced_image.mean(axis=-1)
        return sliced_image
    except Exception as e:
        print(f"Error2: {e}")
        exit(1)


def transpose(path: str) -> list[int]:
    """
    Takes a path to image and transposes it
    """
    try:
        ints = []
        image = zoom(path)
        print(f"The shape of image: {image.shape}")
        for i in range(len(image)):
            ints.append(list(map(lambda x: int(x), image[i])))
        ints = np.array(ints)
        print(ints)
        transposed = image.transpose(1, 0)
        print(f"New shape after Transpose: {transposed.shape}")
        return transposed
    except Exception as e:
        print(f"Error1: {e}")


def main():
    ints = []
    arr = transpose("animal.jpeg")
    for i in range(len(arr)):
        ints.append(list(map(lambda x: int(x), arr[i])))
    ints = np.array(ints)
    print(ints)
    plt.imshow(arr, cmap="gray")
    plt.show()


if __name__ == "__main__":
    main()
