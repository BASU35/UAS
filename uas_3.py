import numpy as np
import cv2 as cv

red  = np.uint8([[[0,0,255 ]]])
hsv_red = cv.cvtColor(red,cv.COLOR_BGR2HSV)
print( hsv_red ) 