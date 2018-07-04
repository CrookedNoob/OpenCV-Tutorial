# -*- coding: utf-8 -*-
"""
Created on Thu Jun 21 21:30:45 2018

@author: ASUS
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Jun 21 21:12:15 2018

@author: ASUS
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Jun 21 20:30:25 2018

@author: ASUS
"""

import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    _,frame = cap.read()
    #HSV - hue sat value
    hsv=cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    lower_red = np.array([150,150,50])
    upper_red = np.array([180,255,255])
    mask= cv2.inRange(hsv, lower_red, upper_red)
    res= cv2.bitwise_and(frame, frame, mask=mask)
    
    kernel=np.ones((5,5), np.uint8)
    erosion= cv2.erode(mask, kernel, iterations=1)
    dilation= cv2.dilate(mask, kernel, iterations=1)
    opening= cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    closing= cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
    
    #We can also use tophat and blackhat
        
    
    cv2.imshow("mask", mask)
    #cv2.imshow("erosion", erosion)
    #cv2.imshow("dilation", dilation)
    cv2.imshow("opening", opening)
    cv2.imshow("closing", closing)
    
    k= cv2.waitKey(5)
    if k==27:
        break
    
cv2.destroyAllWindows()
cap.release()