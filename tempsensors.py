
import Adafruit_ADS1x15
from time import *

GAIN = 1




class TempSensor:
    def initSensor(self):
        return


def initTempSensors():
    adc = Adafruit_ADS1x15.ADS1015()
    while True:
        values = [0]*4
        for i in range(4):
            values[i] = adc.read_adc(i, gain=GAIN)
        print('{2:>4} {3:>4}'.format(*values))
        # Pause for half a second.
        sleep(0.5)