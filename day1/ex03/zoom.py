from matplotlib import pyplot as plt
import numpy as np
from load_image import ft_load


def zoom(path: str) -> list[int]:
    """
    Takes a path to image and zooms it
    param path: path to image
    """
    try:
        image = ft_load(path)
        sliced_image = image[100:500, 450:850]
        sliced_image = sliced_image.mean(axis=-1)
        return sliced_image
    except Exception as e:
        print(f"Error: {e}")
        exit(1)


def main():
    ints = []
    zoomed = zoom("animal.jpeg")
    print(f"The shape after slicing is: {zoomed.shape}")
    for i in range(len(zoomed)):
        ints.append(list(map(lambda x: int(x), zoomed[i])))
    ints = np.array(ints)
    print(ints)
    plt.imshow(zoomed, cmap="gray")
    plt.show()


if __name__ == "__main__":
    main()
