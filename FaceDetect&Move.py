  import cv2
from adafruit_servokit import ServoKit
from time import sleep
############INIT#############

kit = ServoKit(channels=16)
kit.servo[0].angle = 90
frameWidth = 480
frameHeight = 320
cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)
x_medium= int(frameWidth/2)
y_medium = int(frameHeight/2)
center = [int(frameWidth/2),int(frameHeight/2)]
position = 90

faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
sleep(1)
####################################################################
while True:
    success, img = cap.read()
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(imgGray, 1.1, 4)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        x_medium = int((x+x+w)/2)
        y_medium = int((y+y+h)/2)
    cv2.line(img, (x_medium,0), (x_medium , frameHeight), (0,255,0) ,2)
    cv2.line(img, (0,y_medium), (frameWidth,y_medium), (0, 255, 0), 2)

    cv2.imshow("Result", img)



    if cv2.waitKey(1) and 0xFF == ord('q'):
        kit.servo[0].angle = None
        break


    if x_medium < center[0] - 40:
        if position <180:
            position += 2
    elif x_medium > center[0] + 40:
        if position >0:
            position -=2
    print(position)
    kit.servo[0].angle = position

   # kit.servo[0].angle = position