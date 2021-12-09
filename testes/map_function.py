
import cv2
from adafruit_servokit import ServoKit
from time import sleep

import time

from board import SCL, SDA
import busio
from adafruit_motor import servo
from adafruit_pca9685 import PCA9685

i2c = busio.I2C(SCL, SDA)
pca = PCA9685(i2c,address = 0x7f)
pca.frequency = 50

############INIT#############

servo1 = servo.Servo(pca.channels[1], min_pulse=600, max_pulse=2400)
servo0= servo.Servo(pca.channels[0], min_pulse=1000, max_pulse=2000)

frameWidth = 320
frameHeight = 240
cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)
x_medium= int(frameWidth/2)
y_medium = int(frameHeight/2)
center = [int(frameWidth/2),int(frameHeight/2)]
positionX = 90
positionY = 20
camera_angle = 150
servo0.angle = positionX
sleep(1)
faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")


def _map(x, in_min, in_max, out_min, out_max):
    return int((x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)
	

####################################################################
while True:
    success, img = cap.read()
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(imgGray, 1.1, 4)

    for (x, y, w, h) in faces:
        cv2.rectangle(imgGray, (x, y), (x + w, y + h), (255, 0, 0), 2)
        x_medium = int((x+x+w)/2)
        y_medium = int((y+y+h)/2)
    cv2.line(imgGray, (x_medium,0), (x_medium , frameHeight), (0,255,0) ,2)
    cv2.line(imgGray, (0,y_medium), (frameWidth,y_medium), (0, 255, 0), 2)

    cv2.imshow("Result", imgGray)

    angle_x = _map(x_medium, 0, frameWidth, -1*(camera_angle/2), (camera_angle/2))
    if angle_x < -15  or angle_x >15:
        positionX = int(positionX - angle_x*0.2)

    if positionX >180:
        positionX = 180
    elif positionX <0:
        positionX = 0
    print(positionX)

    servo0.angle = positionX

    if cv2.waitKey(1) and 0xFF == ord('q'):
        break








# TEST