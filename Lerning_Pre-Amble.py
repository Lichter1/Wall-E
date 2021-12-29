import serial
from time import sleep
import JoyStickModule as js


def _map(x, in_min, in_max, out_min, out_max):
    return int((x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)


if __name__ == '__main__':
    ser = serial.Serial('/dev/ttyACM0',9600, timeout=1)
    ser.flush()
    while True:
        
        
        #### Read joyStick ##
        jsVal = js.getJS()
        
        if ser.in_waiting > 0:
            ### Map joyStick to angle ###
            angle = str(int(_map(jsVal['axis3'], 1, -1,0, 180)))
            
            ### Print angle in the serial ###
            print (test.encode('utf-8'))
            ser.write(test.encode('utf-8'))
        
        sleep(0.1)
        
        ### If "F5" on joyStick presst, exit ###
        if jsVal['4'] == 1:
            break
