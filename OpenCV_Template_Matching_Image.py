# -*- coding: utf-8 -*-
"""
Created on Thu Jun 21 23:22:57 2018

@author: ASUS
"""

import cv2
import numpy as np

img_bgr= cv2.imread("C:\\Users\\ASUS\\Pictures\\opencv-template-matching-python-tutorial.jpg")
img_gray= cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)

template= cv2.imread("C:\\Users\\ASUS\\Pictures\\opencv-template-matching-python-tutorial-template.jpg")
template= cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
w,h=template.shape[::-1]

res= cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
threshold=0.8
loc= np.where(res>=threshold)

for pt in zip(*loc[::-1]):
    cv2.rectangle(img_bgr, pt, (pt[0]+w, pt[1]+h), (0,255,255),1)
    

cv2.imshow("detected", img_bgr)
cv2.waitKey(0)
cv2.destroyAllWindows()

