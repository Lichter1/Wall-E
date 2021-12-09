from gpiozero import Servo
import math
from time import sleep

from gpiozero.pins.pigpio import PiGPIOFactory

factory = PiGPIOFactory()

servo = Servo(2, min_pulse_width=1/1000, max_pulse_width=2/1000, pin_factory=factory)
servo.value=0
sleep(1)
servo.value=None
#while True:
   # for i in range(0, 360):
  #      servo.value = math.sin(math.radians(i))
  #      sleep(0.01)