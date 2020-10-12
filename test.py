import cv2  
import numpy as np
from PIL import Image
import sys
import os

video = cv2.VideoCapture("green.mov")

out = cv2.VideoWriter('output.avi', cv2.VideoWriter_fourcc('D','I','V','X'), 25.0, (480,360))

u_green = np.array([90, 255, 255]) 
l_green = np.array([40, 20, 20]) 

while True: 
  
    ret, frame = video.read() 
  
    frame = cv2.resize(frame, (480,360))

    # hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

  
    # mask = cv2.inRange(hsv, l_green, u_green) 
    # maks_inv = cv2.bitwise_not(mask)

    # fg = cv2.bitwise_and(frame, frame, mask=maks_inv)
    # res = cv2.bitwise_and(frame, frame, mask = mask) 
  
    # f = frame - res

    rgbaFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA);

    height, width, channels = rgbaFrame.shape

    for x in range(0, height) :
     for y in range(0, width) :
        if (rgbaFrame[x,y,2] > 40 or rgbaFrame[x,y,2] < 90) and (rgbaFrame[x,y,1] > 20 or rgbaFrame[x,y,1] < 255) and (rgbaFrame[x,y,0] > 20 or rgbaFrame[x,y,0] < 255) :
          rgbaFrame[x,y,2] = 80 # R
          rgbaFrame[x,y,1] = 255 # G
          rgbaFrame[x,y,0] = 255 # B

    # for export
    # out.write(f)
    out.write(rgbaFrame)
    
    cv2.imshow("video", frame) 
    cv2.imshow("rgba mask", rgbaFrame) 
  
    if cv2.waitKey(25) == 27: 
        break 
  
video.release() 
out.release()
cv2.destroyAllWindows() 