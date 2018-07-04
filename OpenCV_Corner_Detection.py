# -*- coding: utf-8 -*-
"""
Created on Fri Jun 22 00:19:58 2018

@author: ASUS
"""
import cv2
import numpy as np

img= cv2.imread("C:\\Users\\ASUS\\Pictures\\opencv-corner-detection-sample.jpg")
gray= cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

gray= np.float32(gray)

corners= cv2.goodFeaturesToTrack(gray, 100, 0.01, 10)
corners=np.int0(corners)


for corner in corners:
    x,y = corner.ravel()
    cv2.circle(img, (x,y), 3, (0,255,255), -1)


cv2.imshow("corner", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Used to track objects motion