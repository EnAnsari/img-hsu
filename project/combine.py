import numpy as np
import cv2

# Create example matrices for each RGB channel
width, height = 300, 200  # Define dimensions of the image
blue_channel = np.zeros((height, width), dtype=np.uint8)  # Blue channel matrix
green_channel = np.zeros((height, width), dtype=np.uint8)  # Green channel matrix
red_channel = np.zeros((height, width), dtype=np.uint8)  # Red channel matrix

# Fill each channel matrix with different intensity values for visualization
blue_channel[:, :] = 255  # Set all pixels to maximum intensity (blue)
green_channel[:, :] = 128  # Set all pixels to a moderate intensity (green)
red_channel[:, :] = 64  # Set all pixels to a lower intensity (red)

# Merge the three channels into a single image
merged_image = cv2.merge((blue_channel, green_channel, red_channel))

# Display the merged image
cv2.imshow('Merged Image', merged_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
