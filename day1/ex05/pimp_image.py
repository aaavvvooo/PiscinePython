import numpy as np
from matplotlib import pyplot as plt


def ft_invert(array):
    """Inverts all the colors of the image"""
    image = 255 - array
    plt.imshow(image)
    plt.show()


def ft_red(array):
    """Keeps only red channel"""
    red_ch = array[:, :, 0]
    image = np.zeros_like(array)
    image[:, :, 0] = red_ch
    plt.imshow(image)
    plt.show()


def ft_green(array):
    """Keeps only green channel"""
    green_ch = array[:, :, 1]
    image = array.copy()
    image[:, :, 0] = 0
    image[:, :, 2] = 0
    image[:, :, 1] = green_ch
    plt.imshow(image)
    plt.show()


def ft_blue(array):
    """Keeps only blue channel"""
    blue_ch = array[:, :, 2]
    image = np.zeros_like(array)
    image[:, :, 2] = blue_ch
    plt.imshow(image)
    plt.show()


def ft_grey(array):
    red_ch = array[:, :, 0] / 3
    green_ch = array[:, :, 1] / 3
    blue_ch = array[:, :, 2] / 3
    grey_ch = red_ch + green_ch + blue_ch
    grey_image = np.stack([grey_ch, grey_ch, grey_ch], axis=2)
    plt.imshow(grey_image.astype(np.uint32))
    plt.show()
