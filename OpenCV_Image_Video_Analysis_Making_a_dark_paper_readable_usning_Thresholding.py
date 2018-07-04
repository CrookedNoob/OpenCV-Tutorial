# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 02:50:56 2018

@author: ASUS
"""

import cv2
import numpy as np

img= cv2.imread('C:\\Users\\ASUS\\Pictures\\bookpage.jpg')


#Applying Threshold
retval, threshold= cv2.threshold(img, 12,255, cv2.THRESH_BINARY)

grayscaled=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
retval2, threshold2= cv2.threshold(grayscaled, 12,255, cv2.THRESH_BINARY)
gaus=cv2.adaptiveThreshold(grayscaled,255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 2 )


cv2.imshow('bookbage', img)
cv2.imshow('threshold', threshold)
cv2.imshow('threshold2', threshold2)
cv2.imshow('gaus', gaus)
cv2.waitKey(0)
cv2.destroyAllWindows()



img2= cv2.imread('C:\\Users\\ASUS\\Pictures\\titanic.jpeg')


#Applying Threshold
grayscaled2=cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
gaus2=cv2.adaptiveThreshold(grayscaled2,255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 90, 1 )


cv2.imshow('bookbage', img)
cv2.imshow('threshold', threshold)
cv2.imshow('threshold2', threshold2)
cv2.imshow('gaus', gaus)
cv2.imshow('gaus2', gaus2)
cv2.waitKey(0)
cv2.destroyAllWindows()
