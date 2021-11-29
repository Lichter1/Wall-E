from MotorModule import Motor
import KeyPressModule as kp
#import JoyStickModule as js
from time import sleep
from WebcamModule import getImg
import cv2
from gpiozero.pins.pigpio import PiGPIOFactory
#from ServoModule import Head
from adafruit_servokit import ServoKit


##############################
motor = Motor(22,27,17,2,3,4)
kit = ServoKit(channels=16)

movement = 'KeyBoard'  #[KeyBoard,Joystick]
##############################
#Head.init(18)
kit.servo[0].angle = 90
kp.init()
position = 90

def main():
    img = getImg()
    cv2.imshow('IMG',img)
    key = cv2.waitKey(1)
    if movement == 'Joystick':
       print(js.getJS())
       jsVal = js.getJS()
       motor.move(jsVal['axis2'],jsVal['axis1'],0.1)

    else:
        if kp.getKey('UP'):
            motor.move(1,0,0.1)
        elif kp.getKey('DOWN'):
            motor.move(-1,0,0.1)
        elif kp.getKey('RIGHT'):
            motor.move(1,2,0.1)
        elif kp.getKey('LEFT'):
            motor.move(1,-2,0.1)
        else:
            motor.stop(0.01)
       ###################### HEAD ###################
        kit.servo[0].angle = position




if __name__ == '__main__':
    while True:
         main()