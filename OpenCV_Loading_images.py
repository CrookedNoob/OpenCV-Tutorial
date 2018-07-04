# -*- coding: utf-8 -*-
"""
Created on Mon Jun 18 21:33:29 2018

@author: ASUS
"""

import cv2
import matplotlib.pyplot as plt 
import numpy as np

img=cv2.imread('C:\\Users\\ASUS\\Pictures\\my_watch.jpg', cv2.IMREAD_GRAYSCALE) #to import in grayscale color
#We can also use 
# IMREAD_COLOR = 1
# IMREAD_UNCHANGED = -1 
#IMREAD_GRAYSCALE = 0
print(img)


#img=cv2.imread('C:\\Users\\ASUS\\Pictures\\my_watch.jpg') #to import in colo nut will remove alpha - it is the degree of opaqueness
#print(img)

#matplotlib uses RGB but OpenCV uses BGR
#so it will be a 4D due to BGR+alpha
#Thus gray scale is easier

#Display img using cv2
cv2.imshow('My casio watch', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Display img using matplotlib
plt.imshow(img, cmap='gray', interpolation='bicubic')
#plt.plot([50,100],[80,100], 'c', linewidth=5) to draw line
plt.show()

cv2.imwrite('C:\\Users\\ASUS\\Pictures\\my_watch_gray.jpg', img)