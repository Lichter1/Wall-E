
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
pAngle_x =0
Iangle_x = 0
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
#faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")


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
		cx = x + w//2
		cy = y + h//2
		area = w*h
		myFacesListC.append([cx,cy])
		myFaceListArea.append(area)
	if len(myFaceListArea) != 0:
		i = myFaceListArea.index(max(myFaceListArea))
		# index of closest face
		return img,[myFacesListC[i],myFaceListArea[i]]
	else:
		return img, [[0,0],0]

def trackFace(cx,w,pid,pangle_x):
	print(cx)
	# Current Value - Target Value
	angle_x = _map(cx, 0, frameWidth, -1*(camera_angle/2), (camera_angle/2))
	addAngle = int(pid[0]*angle_x + pid[1] * (angle_x-pangle_x) + pid[2]*(Iangle_x+angle_x)
      	
	if cx[0][0] != 0:
		positionX = int(positionX - addAngle)
		np.clip(positionX,0,180)
		servo0.angle = positionX
		return angle_x

	else:
		servo0.angle = None
		break

	

####################################################################
while True:
    success, img = cap.read()

    img , info = findFace(img,frameWidth,pid

    pAngle_x = trackFace(myDrone,c,w,pid,pAngle_x)

    print(info[0][0])

    cv2.imshow("Result", img)

    angle_x = _map(cx, 0, frameWidth, -1*(camera_angle/2), (camera_angle/2))
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
