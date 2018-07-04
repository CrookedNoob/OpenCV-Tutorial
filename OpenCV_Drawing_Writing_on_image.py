# -*- coding: utf-8 -*-
"""
Created on Mon Jun 18 22:42:46 2018

@author: ASUS
"""

import numpy as np
import cv2


img= cv2.imread('C:\\Users\\ASUS\\Pictures\\my_watch.jpg', cv2.IMREAD_COLOR)

cv2.line(img,(0,0),(150,150),(230,100,200), 15) #Line
cv2.rectangle(img,(20,50), (100,150),(255,0,0), 5) #Rectangle
cv2.circle(img, (100,100), 30, (0,255,0), 3) #Circle - If we use -1, it will fill the circle

#Adding polygons - 1st define the points in an annay
pts=np.array([[10,5],[50,10],[100,180], [30,160], [200,200]], np.int32)
cv2.polylines(img,[pts], True, [0,0,255],3)

#Adding words
font=cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'OpenCV', (0,130), font, 2, (100,100,0), 2, cv2.LINE_AA )

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

