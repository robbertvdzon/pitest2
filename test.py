import I2C_LCD_driver
import Adafruit_ADS1x15
import RPi.GPIO as GPIO
from time import *

mylcd = I2C_LCD_driver.lcd()
mylcd.lcd_display_string("Hello World4!", 1)
adc = Adafruit_ADS1x15.ADS1015()
GAIN = 1
counter = 1

# start code voor encoder
counter = 10  # starting point for the running directional counter
Enc_A = 23  # Encoder input A: input GPIO 23 (active high)
Enc_B = 24  # Encoder input B: input GPIO 24 (active high)

def initEncoder():
    global counter
    print "Rotary Encoder Test Program"
    GPIO.setwarnings(True)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(Enc_A, GPIO.IN) # pull-ups are too weak, they introduce noise
    GPIO.setup(Enc_B, GPIO.IN)
    GPIO.add_event_detect(Enc_A, GPIO.RISING, callback=rotation_decode, bouncetime=2) # bouncetime in mSec
    return


def rotation_decode(Enc_A):
    global counter
    sleep(0.002) # extra 2 mSec de-bounce time
    Switch_A = GPIO.input(Enc_A)
    Switch_B = GPIO.input(Enc_B)
    if (Switch_A == 1) and (Switch_B == 0) : # A then B ->
        counter += 1
        print "direction -> ", counter
        # mylcd.lcd_display_string(str(counter), 1)
        # at this point, B may still need to go high, wait for it
        while Switch_B == 0:
            Switch_B = GPIO.input(Enc_B)
        # now wait for B to drop to end the click cycle
        while Switch_B == 1:
            Switch_B = GPIO.input(Enc_B)
        return
    elif (Switch_A == 1) and (Switch_B == 1): # B then A <-
        counter -= 1
        print "direction <- ", counter
        # mylcd.lcd_display_string(str(counter), 1)
        # A is already high, wait for A to drop to end the click cycle
        while Switch_A == 1:
            Switch_A = GPIO.input(Enc_A)
        return
    else: # discard all other combinations
        return
# end code voor encoder

print('Reading ADS1x15 values, press Ctrl-C to quit...')
# Print nice channel column headers.
print('| {0:>6} | {1:>6} | {2:>6} | {3:>6} |'.format(*range(4)))
print('-' * 37)
# Main loop.
try:
    initEncoder()
    while True:
        values = [0]*4
        for i in range(4):
            values[i] = adc.read_adc(i, gain=GAIN)
        print('{2:>4} {3:>4}'.format(*values))
        mylcd.lcd_clear()
        mylcd.lcd_display_string(str(counter), 1)
        mylcd.lcd_display_string('{2:>6}{3:>6}'.format(*values), 2)
        mylcd.lcd_display_string("menu1", 3)
        mylcd.lcd_display_string("menu2", 4)
        # Pause for half a second.
        sleep(0.5)
except KeyboardInterrupt: # Ctrl-C to terminate the program
        GPIO.cleanup()

