#!/usr/bin/env python

from gpiozero import PWMLED, LED
from gpiozero.tools import random_values
from signal import pause

star = LED(14)

lights = [PWMLED(15), PWMLED(18), PWMLED(23), PWMLED(24), PWMLED(25), PWMLED(8), PWMLED(7), PWMLED(12), PWMLED(16), PWMLED(20)]

star.on()

for i in range (10):
    lights[i].source = random_values()

pause()