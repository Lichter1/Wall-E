import serial
from time import sleep
import JoyStickModule as js

def _map(x, in_min, in_max, out_min, out_max):
    return int((x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)

def ax_map(x,motor):
    if motor == "Servo":
        angle = int(_map(x,-1,1,0,180))
        return angle
    else:
        speed = int(_map(x, -1, 1, -255, -255))
        return speed
if __name__ == '__main__':
    ser = serial.Serial('/dev/ttyACM0',9600, timeout=1)
    ser.flush()
    while True:

        Ready = False

        while Ready == False:
            line = ser.readline().decode('utf-8').rstrip()
            print(line)
            if line == "Start":
                Ready = True


        ### Print command in the serial ###
        jsVal = js.getJS()
        Command = str(ax_map((jsVal['axis1']),"motor")+ " " + str(ax_map((jsVal['axis2']),"motor")+ " " + str(ax_map((jsVal['axis1']),"Servo")+ " " + str(ax_map((jsVal['axis1']),"Servo")
        ser.write(Command.encode('utf-8'))
        ArduinoCom = ser.readline().decode('utf-8').rstrip()
        print(ArduinoCom)