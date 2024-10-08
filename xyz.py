import cv2
import numpy as ny 
import matplotlib 

img = cv2.imread("/Users/dk/Downloads/uas takimages/1.png",cv2.IMREAD_GRAYSCALE)
cv2.imshow("test1",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

