#!/usr/bin/python

#
# Simple CMD Script for LCD Displays for Raspberry Pi
# Usage:
# sudo ./lcdcmd.py "Raspberry @ Fiae.ws" " " " Original Script by" "      Adafruit"
#

import sys
from Adafruit_CharLCD import Adafruit_CharLCD
from subprocess import * 
from time import sleep, strftime
from datetime import datetime

lcd = Adafruit_CharLCD()
lcd.begin(16,4)
lcd.clear()

print '\nLines:'
sys.argv.remove(sys.argv[0])
for item in sys.argv:
	print item
	lcd.message(''+item+'\n')

print 'Done.'

