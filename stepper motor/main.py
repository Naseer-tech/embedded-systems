from machine import Pin
from time import sleep_us

step = Pin(18, Pin.OUT)
direction = Pin(19, Pin.OUT)

direction.value(0)

while True:
    step.value(1)
    sleep_us(500)

    step.value(0)
    sleep_us(500)
