import cv2
import numpy as np

def separate_rgb(image_path):
    # Read the image
    image = cv2.imread(image_path)

    # Split the image into its three channels
    blue_channel, green_channel, red_channel = cv2.split(image)
    print(blue_channel.shape)
    # for line in blue_channel:
    #     for num in line:
    #         print(num, end=' ')
    #     print()


    # Merge the three channels into a single RGB image
    # merged_image = cv2.merge((blue_channel, green_channel, red_channel))

    # # Display the merged image
    # cv2.imshow('Merged Image', merged_image)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()


    # # Display each channel separately
    # cv2.imshow('Blue Channel', blue_channel)
    # cv2.imshow('Green Channel', green_channel)
    # cv2.imshow('Red Channel', red_channel)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

# Example usage
image_path = '../assets/MIT-campus-STATA-1024x768.jpg'  # Path to your image
separate_rgb(image_path)
