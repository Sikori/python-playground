import cv2
cap = cv2.VideoCapture("green.mov")

cap.set(cv2.CAP_PROP_CONVERT_RGB, 0)

count = 0

while True:
    success, frame = cap.read()
    image = cv2.imwrite("frame%d.jpg" % count, frame)
    print(image)
    count += 1
    if cv2.waitKey(25) == 27: 
        break 