#!/usr/bin/env python
""" 
demonstrate easy GPIO use with external breadboard LED through 470 ohm resistor
tested with BBIO 0.0.20 
program functionality:
1) wait for HIGH to be input on P8_13 (e.g. via pushbutton)
2) upon rising edge on P8_13, flash LED at 5Hz, 50% duty
3) upon next rising edge on P8_13, stop flashing LED
4) repeat until Ctrl C pressed
prereq:
sudo pip install --upgrade Adafruit_BBIO
"""
import Adafruit_BBIO.GPIO as gpio
from time import sleep

inp = 'P8_13'
outp = 'P8_14'
flash = False

def main():
    # I/O is bidirectional, so assign in/out
    gpio.setup(inp,gpio.IN) #pushbutton
    gpio.add_event_detect(inp,gpio.RISING,
                          callback=flipled, bouncetime=200) #setup interrupt
    gpio.setup(outp, gpio.OUT) #to LED

    try:
        while True:
            ledflash(flash)
    except KeyboardInterrupt:
        gpio.output(outp,gpio.LOW)
        exit(0)

def flipled(h):
    global flash
    #print('change detect')
    flash= not flash

def ledflash(flash):
    if flash:
        gpio.output(outp,gpio.HIGH) #LED on
        sleep(0.1) #seconds
        gpio.output(outp,gpio.LOW) #LED off
        sleep(0.1)
    else:
        gpio.output(outp,gpio.LOW)

if __name__ == '__main__':
    main()
