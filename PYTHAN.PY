import cv2 as cv
import numpy as np
 
IMG = cv.imread("/Users/dk/Downloads/uas takimages/1.png")
frame = IMG
while(1):
 
    # # Take each frame
    # _, frame = IMG.read()
 
    # Convert BGR to HSV
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
 
    # define range of blue color in HSV
    lower_blue = np.array([40,40,40])
    upper_blue = np.array([80,255,25])
 
    # Threshold the HSV image to get only blue colors
    mask = cv.inRange(hsv, lower_blue, upper_blue)
 
    # Bitwise-AND mask and original image
    res = cv.bitwise_and(frame,frame, mask= mask)
 
    cv.imshow('frame',frame)
    cv.imshow('mask',mask)
    cv.imshow('res',res)
    k = cv.waitKey(5) & 0xFF
    if k == 27:
        break
 
cv.destroyAllWindows()