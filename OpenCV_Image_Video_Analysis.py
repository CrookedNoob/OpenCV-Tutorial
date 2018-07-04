# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 01:24:50 2018

@author: ASUS
"""

import numpy as np
import cv2

img= cv2.imread('C:\\Users\\ASUS\\Pictures\\my_watch.jpg',cv2.IMREAD_COLOR)

#to find the actual color value of a pixel
px=img[55,55]
print(px)

#change pixel color
img[55,55] = [255,255,255]
px= img[55,55]
print(px)

#ROI - REGION OF IMAGE
roi=img[100:150,100:150]
print(roi) #It will print the color of all the pixel values in roi


#To change the color of a block
img[100:150,100:150]=[255,255,255]
cv2.imshow('img', img)

#Move a roi from one region to another1

watch_face = img[37:111,107:194]
img[0:74, 0:87]= watch_face
cv2.imshow('img', img)


cv2.waitKey(0)
cv2.destroyAllWindows()