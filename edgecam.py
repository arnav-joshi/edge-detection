import numpy as np
import cv2
from matplotlib import pyplot as plt
cap = cv2.VideoCapture(0)
cap.set(3,1280)
def on_trackbar(val):
  ret, frame=cap.read()
  img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
  mint = cv2.getTrackbarPos("min", "levels")
  maxt = cv2.getTrackbarPos("max", "levels")
  edges = cv2.Canny(img,mint,maxt)
  cv2.imshow(levels,img)
  cv2.imshow(levels,img) 
  

  cv2.namedWindow("levels")
cv2.createTrackbar("min", "levels", 0, 500, on_trackbar) 
cv2.createTrackbar("max", "levels", 0, 500, on_trackbar) 

cv2.waitKey()
