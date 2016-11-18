#!/usr/bin/env python

from gpiozero import LED
from time import sleep

star = LED(14)

lights = [LED(15), LED(18), LED(23), LED(24), LED(25), LED(8), LED(7), LED(12), LED(16), LED(20)]

star.on()

while True:
    for i in range(3):
        lights[i].toggle()
    sleep(0.5)
    for i in range(3):
        lights[i+3].toggle()
    sleep(0.5)
    for i in range(2):
        lights[i+6].toggle()
    sleep(0.5)
    for i in range(2):
        lights[i+8].toggle()
    sleep(0.5)
