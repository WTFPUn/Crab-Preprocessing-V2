import matplotlib.pyplot as plt
import numpy as np
import cv2


import numpy as np
import matplotlib.pyplot as plt


def show_images(images: np.array):
    """
    Display multiple images in a single figure.

    Parameters:
    images (np.array): An array of images to be displayed.

    Returns:
    None
    """
    fig, axes = plt.subplots(1, len(images), figsize=(15, 15))
    for i, image in enumerate(images):
        axes[i].imshow(image)
        axes[i].axis("off")
    plt.show()


def condition_display(
    image, channel_cond_lower: np.array, channel_cond_upper: np.array
):
    """
    Apply channel condition to an image and return the masked image.

    Args:
            image (np.array): The input image.
            channel_cond_lower (np.array): The lower channel condition values.
            channel_cond_upper (np.array): The upper channel condition values.

    Returns:
            np.array: The masked image after applying the channel condition.
    """
    if (
        image.shape[2] != channel_cond_lower.shape[0]
        or image.shape[2] != channel_cond_upper.shape[0]
    ):
        raise ValueError(
            "channel condition length should be equal to image channel length"
        )

    # bitwsie and operation
    mask = cv2.inRange(image, channel_cond_lower, channel_cond_upper)
    masked_image = cv2.bitwise_and(image, image, mask=mask)

    return masked_image


def plot_distribution(image, channel_name=["Red", "Green", "Blue"]):
    """
    Plot the histogram distribution of each channel in an image.

    Parameters:
    image (numpy.ndarray): The input image.
    channel_name (list, optional): The names of the channels. Default is ["Red", "Green", "Blue"].

    Returns:
    None
    """

    fig, axes = plt.subplots(1, 3, figsize=(15, 5))
    for i, ax in enumerate(axes):
        ax.hist(image[:, :, i].ravel(), bins=256, color="r")
        ax.set_title(f"{channel_name[i]} channel")

    plt.show()


def compare_display(
    img1: np.array, img2: np.array, title1: str = "Original", title2: str = "Processed"
):
    """
    Display two images side by side for comparison.

    Parameters:
    img1 (np.array): The first image.
    img2 (np.array): The second image.
    title1 (str): The title of the first image.
    title2 (str): The title of the second image.

    Returns:
    None
    """
    fig, axes = plt.subplots(1, 2, figsize=(15, 15))
    axes[0].imshow(img1)
    axes[0].set_title(title1)
    axes[0].axis("off")
    axes[1].imshow(img2)
    axes[1].set_title(title2)
    axes[1].axis("off")
    plt.show()
