import cv2  
import numpy as np  

video = cv2.VideoCapture("green.mp4")

# try to use FRWA (alpha channel)
out = cv2.VideoWriter('output.mov', cv2.VideoWriter_fourcc('a','p','4','h'), 25.0, (1280,720))

u_green = np.array([90, 255, 255]) 
l_green = np.array([40, 20, 20]) 

while True: 
  
    ret, frame = video.read() 
  
    frame = cv2.resize(frame, (1280, 720))

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

  
    mask = cv2.inRange(hsv, l_green, u_green) 
    # maks_inv = cv2.bitwise_not(mask)

    # fg = cv2.bitwise_and(frame, frame, mask=maks_inv)
    res = cv2.bitwise_and(frame, frame, mask = mask) 
  
    f = frame - res

    # for export
    out.write(f)

    
    cv2.imshow("video", frame) 
    cv2.imshow("mask", f) 
  
    if cv2.waitKey(25) == 27: 
        break 
  
video.release() 
out.release()
cv2.destroyAllWindows() 