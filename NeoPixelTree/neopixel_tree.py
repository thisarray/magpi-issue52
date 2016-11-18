#!/usr/bin/env python

from neopixel import *
from gpiozero import Button
from time import sleep

button = Button (18)

LED_COUNT      = 30      # Number of LED pixels.
LED_PIN        = 14      # GPIO pin
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz
LED_DMA        = 5
LED_BRIGHTNESS = 255     # Brightness of LEDs
LED_INVERT     = False

def lights_on (strip, color):
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
        strip.show()

def lights_wave(strip, color1, color2):
    for q in range(3):
        for i in range(0, strip.numPixels(), 3):
            strip.setPixelColor(i+q, color1)
        strip.show()
        sleep(0.2)
        for i in range(0, strip.numPixels(), 3):
            strip.setPixelColor(i+q, color2)

def color_wheel(pos):
    if pos < 85:
        return Color(pos * 3, 255 - pos * 3, 0)
    elif pos < 170:
        pos -= 85
        return Color(255 - pos * 3, 0, pos * 3)
    else:
        pos -= 170
        return Color(0, pos * 3, 255 - pos * 3)

def lights_rainbow(strip):
    for j in range(256):
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, color_wheel(((i * 256 / strip.numPixels()) + j) & 255))
        strip.show()
        sleep(0.1)

strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)
strip.begin()

while True:
    lights_on(strip, Color(255,255,255))
    button.wait_for_press()
    sleep(0.5)
    while button.is_pressed == False:
        lights_wave(strip, Color(255,0,0), Color(0,0,255))
    sleep(0.5)
    while button.is_pressed == False:
        ligthts_rainbow(strip)
    sleep(0.5)
    
