def pixel_interpolate(image):
    image = image.copy()
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            if image[i, j, 0] == 0 and image[i, j, 1] == 0 and image[i, j, 2] == 0:
                nearest_pixels = [image]
