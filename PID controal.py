import cv2
from adafruit_servokit import ServoKit
from time import sleep
import numpy as np
import time

from board import SCL, SDA
import busio
from adafruit_motor import servo
from adafruit_pca9685 import PCA9685

i2c = busio.I2C(SCL, SDA)
pca = PCA9685(i2c, address=0x7f)
pca.frequency = 50

############INIT#############

servo1 = servo.Servo(pca.channels[1], min_pulse=800, max_pulse=2200)
servo0 = servo.Servo(pca.channels[0], min_pulse=800, max_pulse=2200)
servo2 = servo.Servo(pca.channels[2], min_pulse=800, max_pulse=2200)
pAngle_x = [0,0,90,50, 60]
Iangle_x = 0
Iangle_y = 0
frameWidth = 320
frameHeight = 240
cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)
x_medium = int(frameWidth / 2)
y_medium = int(frameHeight / 2)
center = [int(frameWidth / 2), int(frameHeight / 2)]
positionX = 150
positionY = 20
camera_angle = 150
servo0.angle = positionX
sleep(1)
pid = [0.1,0.05,0.5]

# faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")


def _map(x, in_min, in_max, out_min, out_max):
    return int((x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)


def findFace(img):
    faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(imgGray, 1.1, 4)

    myFacesListC = []
    myFaceListArea = []

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        cx = x + w // 2
        cy = y + h // 2
        area = w * h
        myFacesListC.append([cx, cy])
        myFaceListArea.append(area)
    if len(myFaceListArea) != 0:
        i = myFaceListArea.index(max(myFaceListArea))
        cv2.line(img, (myFacesListC[i][0],0), (myFacesListC[i][0] , frameHeight), (0,255,0) ,1)
        cv2.line(img, (0,myFacesListC[i][1]), (frameWidth,myFacesListC[i][1]), (0, 255, 0), 1)
        # index of closest face
        return img, [myFacesListC[i], myFaceListArea[i]]
    else:
        return img, [[0, 0], 0]


def trackFace(c, frameWidth, pid, staf):
    PAX=staf[0]
    PAY=staf[1]
    positionX = int(staf[2])
    positionY = int(staf[3])
    positionY_L= int(staf[4])

    ########################## X axsis ##########################

    if c[0][0] != 0:
        angle_x = _map(c[0][0], 0, frameWidth, -1 * (camera_angle / 2), (camera_angle / 2))
        addAngleX = int((pid[0] * angle_x) + (pid[2] * (angle_x - PAX)) + (pid[1] * (Iangle_x + angle_x)))
        positionX = int(positionX - addAngleX)
        if positionX <0:
            positionX = 0

        elif positionX > 180:
            positionX = 180

        print("positionX",positionX)
        servo0.angle = positionX

    else:
        servo0.angle = None
        angle_x = 0

    ###################################### Y axsis ###################

    if c[0][1] != 0:
        angle_y = _map(c[0][1], 0, frameHeight, -1 * (camera_angle / 2), (camera_angle / 2))
        addAngleY = int((pid[0] * angle_y) + (pid[2] * (angle_y - PAY)) + (pid[1] * (Iangle_y + angle_y)))
        positionY = int(positionY + addAngleY)

        if positionY <0:
            positionY = 0
            positionY_L=positionY_L+5

        elif positionY > 180:
            positionY = 180
            positionY_L=positionY_L-5

        if positionY_L <0:
            positionY_L = 0

        elif positionY_L > 180:
            positionY_L = 180
        print("positionYH",positionY)
        print("positionYL",positionY_L)
        servo1.angle = positionY
        servo2.angle = positionY_L

    else:
        servo1.angle = None
        angle_y = 0

    return angle_x,angle_y,positionX,positionY,positionY_L


####################################################################

if __name__ == '__main__':

    while True:
        ### Get img###
        success, img = cap.read()
        ### Find Face###
        img, info = findFace(img)
        ### Track Face###
        pAngle_x = trackFace(info, frameWidth, pid, pAngle_x)
        dsize = (640,480)
        #print(info[0][0])
        img = cv2.resize(img,dsize)
        cv2.imshow("Result", img)

        #print(positionX)

        if cv2.waitKey(1) and 0xFF == ord('q'):
            break

# TEST