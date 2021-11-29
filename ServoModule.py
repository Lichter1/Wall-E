hubfrom gpiozero import Servo
from time import sleep
from gpiozero.pins.pigpio import PiGPIOFactory
import math
factory = PiGPIOFactory()
import cv2
def empty(a):
    pass

sleep(1)
class Head():
    def init(pmw):
        factory = PiGPIOFactory()
        global servo
        servo = Servo(pmw, min_pulse_width=1/1000, max_pulse_width=2.0/1000, pin_factory=factory)
        servo.value = 0
        sleep(1)
        servo.value = None
        print ('start')



    def move(x,t=0.01):
        servo.value = x
        sleep(t)

    def stop():
        servo.value = None



def main():
    Head.init(18)
    x=100
    y=0
    cv2.namedWindow("TrackBar")
    cv2.resizeWindow("TrackBar",500,300)
    cv2.createTrackbar("Head Angle","TrackBar",100,200,empty)
    cv2.createTrackbar("Head Power","TrackBar",1,1,empty)
    sleep(1)
    while True:
        H_A = cv2.getTrackbarPos("Head Angle","TrackBar")
        H_P = cv2.getTrackbarPos("Head Power","TrackBar")
        if H_P == 0:
            Head.stop()
            print("head stop")

        if H_P == 1:
            if x == H_A:
                if y <15:
                    y=y+1
                #sleep(0.01)
                if y > 10:
                    Head.stop()
                    print("head Nome")
                else:
                    print(H_A)
                    Head.move((H_A/100)-1)
                    print((H_A/100)-1)
            else:
                y=0
                x=H_A
        print(y)
        cv2.waitKey(1)





if __name__ == '__main__':
    main()