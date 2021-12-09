import cv2
import numpy as np

frameWidth = 640
frameHeight = 480
cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()

    cv2.imshow("Frame",frame)

    key = cv2.waitKey

    if key==1:
        break
cap.release()
cv2.destroyAllWindows()