import cv2
import numpy as np

# def pixel_interpolate(image):
# 	image = image.copy()
# 	for i in range(image.shape[0]):
# 		for j in range(image.shape[1]):
# 			if image[i, j, 0] == 0 and image[i, j, 1] == 0 and image[i, j, 2] == 0:
# 				nearest_pixels = [image]


def enhance_contrast(img: np.ndarray) -> np.ndarray:
    """
    Enhances the contrast of an image using histogram equalization.

    Parameters:
    img (numpy.ndarray): The input image.

    Returns:
    numpy.ndarray: The image with enhanced contrast.
    """
    img_yuv = cv2.cvtColor(img, cv2.COLOR_RGB2YUV)
    img_yuv[:, :, 0] = cv2.equalizeHist(img_yuv[:, :, 0])
    img_output = cv2.cvtColor(img_yuv, cv2.COLOR_YUV2RGB)
    return img_output


def color_correct(img):
    """
    Applies color correction to an image.

    Parameters:
    img (numpy.ndarray): The input image.

    Returns:
    numpy.ndarray: The color-corrected image.
    """
    img_hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
    # Adjust hue, saturation, and value as needed
    img_hsv[:, :, 0] = img_hsv[:, :, 0] + 10  # Adjust hue
    img_hsv[:, :, 1] = img_hsv[:, :, 1] * 1.2  # Adjust saturation
    img_hsv[:, :, 2] = img_hsv[:, :, 2] * 1.1  # Adjust value
    img_output = cv2.cvtColor(img_hsv, cv2.COLOR_HSV2RGB)
    return img_output


def unsharp_mask(img, radius, amount, threshold):
    """Apply unsharp masking to enhance image details."""
    blurred = cv2.GaussianBlur(img, (radius, radius), 0)
    sharpened = cv2.addWeighted(img, 1 + amount, blurred, -amount, 0)
    return sharpened
