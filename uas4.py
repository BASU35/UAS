import cv2
import numpy as np

# Load the image
image = cv2.imread('/Users/dk/Downloads/uas takimages/1.png')

# Convert the image to the HSV color space
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Define the range for green color in HSV
lower_green = np.array([40, 40, 40])
upper_green = np.array([80, 255, 255])

# Create a mask for green areas
mask = cv2.inRange(hsv_image, lower_green, upper_green)

# Create an output image to display the green areas
output_image = cv2.bitwise_and(image, image, mask=mask)

# Mark the green areas in the original image
marked_image = cv2.addWeighted(image, 0.7, output_image, 0.3, 0)

# Save the marked image
cv2.imwrite('marked_image.jpg', marked_image)

# Display the original and marked images
cv2.imshow('Original Image', image)
cv2.imshow('mask Image', mask)
cv2.imshow('Marked Image', marked_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
