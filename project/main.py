import cv2
import math
from tqdm import tqdm # type: ignore

C1 = 1
C2 = 1
red_wavelength = 630  # nano meter
blue_wavelength = 532
green_wavelength = 465

def calculate_pseudo_color(channel1, channel2, wavelength1, wavelength2, c1, c2, title):
    """
    Calculates a pseudo-color representation based on two image channels and their wavelengths.

    Args:
        channel1: A NumPy array representing the first image channel.
        channel2: A NumPy array representing the second image channel.
        wavelength1: The wavelength of the first channel in nanometers.
        wavelength2: The wavelength of the second channel in nanometers.
        c1: A constant value
        c2: Another constant value

    Returns:
        A NumPy array representing the pseudo-color image.
    """
    rows, cols = channel1.shape  # Get image dimensions
    result = channel1.copy()  # Create a copy for modification
    # counter = 0
    # Avoid division by zero and potential NaNs
    for row in tqdm(range(rows), desc=title):
        for col in range(cols):
            if channel1[row, col] == 0 or channel2[row, col] == 0:
                result[row, col] = 0
                # counter += 1
                continue
            try:
                result[row, col] = (c2 * ((1 / wavelength1) - (1 / wavelength2))) / (
                    c1 + math.log10(channel1[row, col] / channel2[row, col])
                )
            except ZeroDivisionError:
                result[row, col] = 0  # Handle potential division by zero

    return result


# Load the image
image_path = "../assets/MIT-campus-STATA-1024x768.jpg"  # Replace with your image path
image = cv2.imread(image_path)

# Split channels
blue_channel, green_channel, red_channel = cv2.split(image)

# Generate pseudo-color images
g2r = calculate_pseudo_color(green_channel, red_channel, green_wavelength, red_wavelength, C1, C2, 'creating green with red (line by line)')
g2b = calculate_pseudo_color(green_channel, blue_channel, green_wavelength, blue_wavelength, C1, C2, 'creating green with blue (line by line)')
b2r = calculate_pseudo_color(blue_channel, red_channel, blue_wavelength, red_wavelength, C1, C2, 'creating blue with red (line by line)')

# Display results
cv2.imshow('Green to Red', g2r)
cv2.imshow('Green to Blue', g2b)
cv2.imshow('Blue to Red', b2r)

# cv2.imshow('merged image', cv2.merge([g2b, b2r, g2r]))

cv2.waitKey(0)
cv2.destroyAllWindows()
