import I2C_LCD_driver
# import Adafruit_ADS1x15
# import RPi.GPIO as GPIO
# from time import *
from eventbus import *

class Display:

    def onMessage(self, event, message):
        if (event=="display"):
            self.writeDisplay(message,2)
        print 'got message in display: '+event+' '+message


    def initDisplay(self):
        global mylcd
        global bus
        bus = getEventbus()
        bus.register(self)
        mylcd = I2C_LCD_driver.lcd()
        mylcd.lcd_display_string("Smoker test", 1)
        return

    def writeDisplay(self, text, line):
        global mylcd
        mylcd.lcd_display_string(text, line)

def initDisplay():
    display = Display()
    display.initDisplay()
