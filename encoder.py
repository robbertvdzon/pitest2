from display import *
import I2C_LCD_driver
import Adafruit_ADS1x15
import RPi.GPIO as GPIO
from time import *
from eventbus import *

class Encoder:
    counter = 10  # starting point for the running directional counter
    Enc_A = 19  # Encoder input A: input GPIO 23 (active high) // 23 -> 13
    Enc_B = 13  # Encoder input B: input GPIO 24 (active high) // 24 -> 19

    def onMessage(self, event, message):
        print 'got message in encoder: '+event+' '+message

    def initEncoder(self):
        global counter
        global bus
        bus = getEventbus()
        print 'init encoder'
        GPIO.setwarnings(True)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.Enc_A, GPIO.IN) # pull-ups are too weak, they introduce noise
        GPIO.setup(self.Enc_B, GPIO.IN)
        GPIO.add_event_detect(self.Enc_A, GPIO.RISING, callback=self.rotation_decode, bouncetime=2) # bouncetime in mSec
        bus.register(self)
        return

    def initKnopSensor(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(6, GPIO.IN) # pull-ups are too weak, they introduce noise
        GPIO.add_event_detect(6, GPIO.RISING, callback=self.knopPressedDetected, bouncetime=1000) # bouncetime in mSec
        return


    def knopPressedDetected(self, param):
        global bus
        bus.emit("button pressed","")
        return


    def rotation_decode(self, Enc_A):
        print 'decode'
        global bus
        sleep(0.002) # extra 2 mSec de-bounce time
        Switch_A = GPIO.input(self.Enc_A)
        Switch_B = GPIO.input(self.Enc_B)
        if (Switch_A == 1) and (Switch_B == 0) : # A then B ->
            self.counter += 1
            bus.emit("encoder",str(self.counter))
            bus.emit('display',str(self.counter))
            # mylcd.lcd_display_string(str(counter), 1)
            # at this point, B may still need to go high, wait for it
            while Switch_B == 0:
                Switch_B = GPIO.input(self.Enc_B)
            # now wait for B to drop to end the click cycle
            while Switch_B == 1:
                Switch_B = GPIO.input(self.Enc_B)
            return
        elif (Switch_A == 1) and (Switch_B == 1): # B then A <-
            self.counter -= 1
            bus.emit("encoder",str(self.counter))
            bus.emit('display',str(self.counter))

            # mylcd.lcd_display_string(str(counter), 1)
            # A is already high, wait for A to drop to end the click cycle
            while Switch_A == 1:
                Switch_A = GPIO.input(Enc_A)
            return
        else: # discard all other combinations
            return
            # end code voor encoder

def initEncoder():
    encoder = Encoder()
    encoder.initEncoder()
    encoder.initKnopSensor()
    return
