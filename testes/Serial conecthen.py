import serial

if __name__ == '__main__':
    ser = serial.Serial('/dev/ttyACM0',9600, timeout=1)
    ser.flush()

while True:
        if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8').rstrip()
            print(line)
            if float(line) <= 23:
                ser.write(b"blue\n")
            elif float(line) > 23 and float(line) <= 25:
                ser.write(b"white\n")
            elif float(line) > 25:
                ser.write(b"red\n")
            else:
                ser.write(b"all\n")