from gpiozero import LED
from time import sleep
led = LED(21)
while True:
    led.on()
    print('ON')
    sleep(1)
    led.off()
    print('off')
    sleep(1)