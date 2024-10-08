

import cv2
import numpy as np

def count_triangles(image_path):
    image = cv2.imread(image_path)
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Define color ranges for red and blue
    red_lower = np.array([110, 100, 100])
    red_upper = np.array([ 130, 255, 255])
    blue_lower = np.array([110, 100, 100])
    blue_upper = np.array([130, 255, 255])

    # Create masks for red and blue colors
    red_mask = cv2.inRange(hsv, red_lower, red_upper)
    blue_mask = cv2.inRange(hsv, blue_lower, blue_upper)

    # Find contours for red triangles
    red_contours, _ = cv2.findContours(red_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    red_triangles = [cnt for cnt in red_contours if len(cv2.approxPolyDP(cnt, 0.02 * cv2.arcLength(cnt, True), True)) == 3]

    # Find contours for blue triangles
    blue_contours, _ = cv2.findContours(blue_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    blue_triangles = [cnt for cnt in blue_contours if len(cv2.approxPolyDP(cnt, 0.02 * cv2.arcLength(cnt, True), True)) == 3]

    return len(red_triangles), len(blue_triangles)

# Example usage
red_count, blue_count = count_triangles('/Users/dk/Desktop/Screenshot 2024-10-07 at 1.04.46 PM.png')
print(f'Red triangles: {red_count}, Blue triangles: {blue_count}')


