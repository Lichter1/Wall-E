import serial
from time import sleep
if __name__ == '__main__':
    ser = serial.Serial('/dev/ttyACM0',9600, timeout=1)
    ser.flush()
    while True:
        ser.write(b"0 0 100 0 0 0 180/n")
        sleep(0.5)
        ser.write(b"0 0 110 0 0 180 0/n")
        sleep(0.5)