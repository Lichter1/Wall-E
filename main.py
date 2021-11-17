from MotorModule import Motor
import KeyPressModule as kp
#import JoyStickModule as js
from time import sleep
from WebcamModule import getImg
import cv2
from gpiozero.pins.pigpio import PiGPIOFactory
from ServoModule import Head


##############################
motor = Motor(22,27,17,2,3,4)
movement = 'KeyBoard'  #[KeyBoard,Joystick]
##############################
Head.init(18)
kp.init()

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
        elif kp.getKey('w'):
            Head.move(0.1)
        elif kp.getKey('q'):
            Head.move(0.75)
        elif kp.getKey('e'):
            Head.move(-0.65,0.1)
        else:
            motor.stop(0.1)
            Head.stop()



if __name__ == '__main__':
    while True:
         main()