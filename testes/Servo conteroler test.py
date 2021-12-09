import time

from board import SCL, SDA
import busio
from adafruit_motor import servo
from adafruit_pca9685 import PCA9685

i2c = busio.I2C(SCL, SDA)
pca = PCA9685(i2c,address = 0x7f)
pca.frequency = 50

servo1 = servo.Servo(pca.channels[1], min_pulse=600, max_pulse=2400)
servo0= servo.Servo(pca.channels[0], min_pulse=600, max_pulse=2400)

for i in range(180):
    servo1.angle = 180 - i
    servo0.angle = 180 - i
    time.sleep(0.02)
for i in range(180):
    servo0.angle = i
    servo1.angle = i
    time.sleep(0.02)



fraction = 0.0
while fraction < 1.0:
    servo0.fraction = fraction
    servo1.fraction = fraction
    fraction += 0.01
    time.sleep(0.03)

pca.deinit()