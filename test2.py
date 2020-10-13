import cv2
import numpy as np
import glob

cap = cv2.VideoCapture("green.mov")

cap.set(cv2.CAP_PROP_CONVERT_RGB, 0)

count = 0

success, frame = cap.read()

while success:
    success, frame = cap.read()

    if success:
        frame = cv2.resize(frame, (480,360))
        image = cv2.imwrite("./exports/frame%d.png" % count, frame)
        cv2.imshow("video", frame) 

    count += 1

    if cv2.waitKey(25) == 27: 
        break 

img_array = []
for filename in glob.glob('./exports/*.png'):
    img = cv2.imread(filename)
    img_array.append(img)
    print("read")

out = cv2.VideoWriter('output.avi', cv2.VideoWriter_fourcc('M','J','P','G'), 60, (480,360))
 
for i in range(len(img_array)):
    out.write(img_array[i])

cap.release() 
out.release()
cv2.destroyAllWindows() 