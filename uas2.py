import cv2
import numpy as np

def detect_triangles(image_path):
    # Load the image
    image = cv2.imread(image_path)
    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Apply edge detection
    edges = cv2.Canny(gray, 50, 150, apertureSize=3)
    
    # Find contours
    contours, _ = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    red_count = 0
    blue_count = 0
    
    for contour in contours:
        # Approximate the contour to a polygon
        epsilon = 0.02 * cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, epsilon, True)
        
        # Check if the shape is a triangle
        if len(approx) == 3:
            # Get the color of the triangle
            mask = np.zeros(image.shape[:2], dtype=np.uint8)
            cv2.drawContours(mask, [approx], -1, 255, -1)
            mean_val = cv2.mean(image, mask=mask)
            
            # Check if the triangle is red or blue
            if mean_val[2] > mean_val[1] and mean_val[2] > mean_val[0]:  # Red
                red_count += 1
            elif mean_val[0] > mean_val[1] and mean_val[0] > mean_val[2]:  # Blue
                blue_count += 1

    return red_count, blue_count

# Example usage
red_triangles, blue_triangles = detect_triangles('/Users/dk/Downloads/uas takimages/1.png')
print(f'Red triangles: {red_triangles}, Blue triangles: {blue_triangles}')
