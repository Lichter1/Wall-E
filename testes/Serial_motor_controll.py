import serial
from time import sleep
#import JoyStickModule as js
if __name__ == '__main__':
    ser = serial.Serial('/dev/ttyACM0',9600, timeout=1)
    ser.flush()
    while True:
        #print(js.getJS())
        #jsVal = js.getJS()

        #test = str("0 0")+" "+str(jsVal['axis2'])+" "+str(jsVal['axis1'])+" "+str("20 0 180/n")
        #print (test.encode('utf-8'))
        #ser.write(test.encode('utf-8'))

       #motor.move(jsVal['axis2'],jsVal['axis1'],0.1)

        ser.write(b"0 0 100 50 180 140 90/n")

        sleep(0.1)
        #ser.write(b"0 0 90 50 0 0 180/n")
        #sleep(0.1)