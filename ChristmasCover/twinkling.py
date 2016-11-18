#!/usr/bin/env python

from gpiozero import LED
from random import randint
from time import sleep

star = LED(14)

lights = [LED(15), LED(18), LED(23), LED(24), LED(25), LED(8), LED(7), LED(12), LED(16), LED(20)]

star.on()

for i in range(7):
    lights[i].on()

while True:
    turn_off = randint(0,9)
    turn_on = randint(0,9)
    if lights[turn_off].is_lit == True and lights[turn_on].is_lit == False:
        lights[turn_off].off()
        lights[turn_on].on()
        sleep(0.5)
        
