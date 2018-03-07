from display import *
import I2C_LCD_driver
import Adafruit_ADS1x15
import RPi.GPIO as GPIO
from time import *

class Encoder:
    Enc_A = 19  # Encoder input A: input GPIO 23 (active high) // 23 -> 13
    Enc_B = 13  # Encoder input B: input GPIO 24 (active high) // 24 -> 19
    inputListeners = []

    def __init__(self):
        self.initEncoder()
        self.initKnopSensor()

    def addInputListener(self, listener):
        self.inputListeners.append(listener)

    def initEncoder(self):
        global counter
        GPIO.setwarnings(True)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.Enc_A, GPIO.IN) # pull-ups are too weak, they introduce noise
        GPIO.setup(self.Enc_B, GPIO.IN)
        GPIO.add_event_detect(self.Enc_A, GPIO.RISING, callback=self.rotation_decode, bouncetime=2) # bouncetime in mSec
        return

    def initKnopSensor(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(6, GPIO.IN) # pull-ups are too weak, they introduce noise
        GPIO.add_event_detect(6, GPIO.RISING, callback=self.knopPressedDetected, bouncetime=1000) # bouncetime in mSec
        return


    def knopPressedDetected(self, param):
        for listener in self.inputListeners:
            listener.buttonPressed()


    def rotation_decode(self, Enc_A):
        sleep(0.002) # extra 2 mSec de-bounce time
        Switch_A = GPIO.input(self.Enc_A)
        Switch_B = GPIO.input(self.Enc_B)
        if (Switch_A == 1) and (Switch_B == 0) : # A then B ->
            for listener in self.inputListeners:
                listener.buttonDown()
            while Switch_B == 0:
                Switch_B = GPIO.input(self.Enc_B)
            # now wait for B to drop to end the click cycle
            while Switch_B == 1:
                Switch_B = GPIO.input(self.Enc_B)
            return
        elif (Switch_A == 1) and (Switch_B == 1): # B then A <-
            for listener in self.inputListeners:
                listener.buttonUp()
            while Switch_A == 1:
                Switch_A = GPIO.input(Enc_A)
            return
        else: # discard all other combinations
            return
            # end code voor encoder

