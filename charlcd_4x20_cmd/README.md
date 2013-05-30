This is a simple command line script. It accept one argument per LCD display line.

URLs
----
Adafruit Tutorial: http://learn.adafruit.com/drive-a-16x2-lcd-directly-with-a-raspberry-pi/overview
GPIO Pins: http://elinux.org/RPi_Low-level_peripherals
Original Sourcecode: https://github.com/adafruit/Adafruit-Raspberry-Pi-Python-Code
German Blog Post: http://anwendungsentwickler.ws/blog/kategorien/raspberry-pi/4x20-lcd-screen-mit-dem-raspberry-pi.html

PIN Layout
----------

    Pin #1 of the LCD goes to ground (black wire)
    Pin #2 of the LCD goes to +5V (red wire)
    Pin #3 (Vo) connects to the middle of the potentiometer (orange wire)
    Pin #4 (RS) connects to the Cobber #25 (yellow wire)
    Pin #5 (RW) goes to ground (black wire)
    Pin #6 (EN) connects to cobber #24 (green wire)
    Skip LCD Pins #7, #8, #9 and #10
    Pin #11 (D4) connects to cobber #23 (blue wire)
    Pin #12 (D5) connects to cobber #17 (violet wire)
    Pin #13 (D6) connects to cobber #21 (gray wire) (!!! on rev2 board GPIO 27 !!!)
    Pin #14 (D7) connects to cobber #22 (white wire)
    Pin #15 (LED +) goes to +5V (red wire)
    Pin #16 (LED -) goes to ground (black wire)

Important: This script works only with revision 2 boards!
