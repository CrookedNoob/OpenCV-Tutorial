# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 01:42:33 2018

@author: ASUS
"""
import numpy as np
import cv2


img1=cv2.imread('C:\\Users\\ASUS\\Pictures\\flower_photos\\daisy\\43474673_7bb4465a86.jpg')
img2=cv2.imread('C:\\Users\\ASUS\\Pictures\\flower_photos\\daisy\\153210866_03cc9f2f36.jpg')
img3=cv2.imread('C:\\Users\\ASUS\\Pictures\\TF2.jpg')
img4=cv2.imread('C:\\Users\\ASUS\\Pictures\\TF.jpg')



rows, cols, channels = img3.shape
roi=img1[0:rows,0:cols]

rows, cols, channels = img34shape
roi=img1[0:rows,0:cols]


#Create mask of image 3
img3gray= cv2.cvtColor(img3, cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img3gray, 220,255, cv2.THRESH_BINARY_INV)
mask_inv=cv2.bitwise_not(mask)

ret, mask = cv2.threshold(img3gray, 220,255, cv2.THRESH_BINARY_INV)
mask_inv=cv2.bitwise_not(mask)


cv2.imshow('mask', mask)
cv2.imshow('mask_inv', mask_inv)

img1_bg= cv2.bitwise_and(roi,roi, mask=mask_inv)
img3_fg= cv2.bitwise_and(img3,img3, mask=mask)

dst= cv2.add(img1_bg, img3_fg)
img1[0:rows,0:cols]=dst

cv2.imshow('res',img1)

cv2.imshow('img1_bg', img1_bg)
cv2.imshow('img3_fg`', img3_fg)
cv2.imshow('dst', dst)


cv2.waitKey(0)
cv2.destroyAllWindows()





#Both the images must be of same size
add= img1+img2
cv2.imshow('img`', img1)
cv2.imshow('img2', img2)
cv2.imshow('add', add)

cv2.waitKey(0)
cv2.destroyAllWindows()


add2= cv2.add(img1,img2)
cv2.imshow('add2', add2)

cv2.waitKey(0)
cv2.destroyAllWindows()


weighted=cv2.addWeighted(img1,0.6, img2, 0.4, 0)
cv2.imshow('weighted', weighted)

#To lose opaqueness