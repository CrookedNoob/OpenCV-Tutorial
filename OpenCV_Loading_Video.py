# -*- coding: utf-8 -*-
"""
Created on Mon Jun 18 22:06:03 2018

@author: ASUS
"""

import cv2
import numpy as np

cap= cv2.VideoCapture(0)
fourcc=cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
out= cv2.VideoWriter('C:\\Users\\ASUS\\Videos\\Captures\\OpenCV_Vid_import.avi', fourcc, 20, (640,480))

while True:
    ret, frame = cap.read()
    cv2.imshow('color', frame)
    out.write(frame)
    gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('gray', gray)
    
    if cv2.waitKey(1) & 0xFF== ord('q'):
        break
    
cap.release()
out.release()
cv2.destroyAllWindows()


