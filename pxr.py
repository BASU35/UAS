import cv2
import numpy as np

def detect_buildings(image_path):
    # Load the image
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Use edge detection to find outlines of buildings
    edges = cv2.Canny(gray, 50, 150, apertureSize=3)

    # Find contours of the detected edges
    contours, _ = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Draw contours on the original image
    for contour in contours:
        if cv2.contourArea(contour) > 100:  # Filter out small contours
            cv2.drawContours(image, [contour], -1, (0, 255, 0), 2)

    # Show the result
    cv2.imshow('Detected Buildings', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Example usage
detect_buildings('/Users/dk/Downloads/uas takimages/1.png')
