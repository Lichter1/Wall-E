import cv2
from adafruit_servokit import ServoKit
from time import sleep
import serial
############INIT#############

ser = serial.Serial('/dev/ttyACM0',9600, timeout=1)
ser.flush()
frameWidth = 480
frameHeight = 320
cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)
x_medium= int(frameWidth/2)
y_medium = int(frameHeight/2)
center = [int(frameWidth/2),int(frameHeight/2)]
positionX = 90
positionY = 20

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
        
        break


    if x_medium < center[0] - 40:
        if positionX <180:
            positionX += 2
    elif x_medium > center[0] + 40:
        if positionX >0:
            positionX -=2

    if y_medium < center[1] - 40:
        if positionY < 180:
            positionY += 2
    elif y_medium > center[1] + 40:
        if positionY > 0:
            positionY -= 2


    print(positionX)
    print(positionY)

    ser.write(b"0 0",positionX,positionY,"20 0 180/n")


   # kit.servo[0].angle = position