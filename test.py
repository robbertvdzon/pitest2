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
Enc_A = 23  # Encoder input A: input GPIO 23 (active high) // 23 -> 13
Enc_B = 24  # Encoder input B: input GPIO 24 (active high) // 24 -> 19
KlepSensorPinOpen = 22
KlepSensorPinClosed = 27

def initEncoder():
    global counter
    print "Rotary Encoder Test Program3"
    GPIO.setwarnings(True)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(Enc_A, GPIO.IN) # pull-ups are too weak, they introduce noise
    GPIO.setup(Enc_B, GPIO.IN)
    GPIO.add_event_detect(Enc_A, GPIO.RISING, callback=rotation_decode, bouncetime=2) # bouncetime in mSec
    return

def initKlepSensor():
    print "Klep sensor init"
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(KlepSensorPinOpen, GPIO.IN) # pull-ups are too weak, they introduce noise
    GPIO.setup(KlepSensorPinClosed, GPIO.IN)
    GPIO.add_event_detect(KlepSensorPinOpen, GPIO.FALLING, callback=klepOpenDetected, bouncetime=50) # bouncetime in mSec
    GPIO.add_event_detect(KlepSensorPinClosed, GPIO.FALLING, callback=klepClosedDetected, bouncetime=50) # bouncetime in mSec
    # sleep(10)
    return

def initKnopSensor():
    print "Knop init2"
    GPIO.setmode(GPIO.BCM)
    # GPIO.setup(6, GPIO.OUT)
    # GPIO.output(26, 0)
    GPIO.setup(6, GPIO.IN) # pull-ups are too weak, they introduce noise
    GPIO.add_event_detect(6, GPIO.RISING, callback=knopPressedDetected, bouncetime=1000) # bouncetime in mSec
    return

def testPWM():
    GPIO.setmode(GPIO.BCM)  # choose BCM or BOARD numbering schemes. I use BCM
    GPIO.setup(12, GPIO.OUT)# set GPIO 25 as an output. You can use any GPIO port
    # GPIO.output(25, GPIO.LOW)
    # print('low')
    # sleep(5)
    # GPIO.output(25, GPIO.HIGH)
    # print('high')
    # sleep(5)


    p = GPIO.PWM(12, 50)    # create an object p for PWM on port 25 at 50 Hertz
    # you can have more than one of these, but they need
    # different names for each port
    # e.g. p1, p2, motor, servo1 etc.
    print('init')
    sleep(5)
    print('20')
    p.start(20)             # start the PWM on 50 percent duty cycle, duty cycle value can be 0.0 to 100.0%, floats are OK
    sleep(5)
    print('90')
    p.start(90)             # start the PWM on 50 percent duty cycle, duty cycle value can be 0.0 to 100.0%, floats are OK
    sleep(5)
    # print('70')
    # p.ChangeDutyCycle(70)   # change the duty cycle to 90%
    # sleep(5)
    # print('100')
    # p.ChangeDutyCycle(100)  # change the frequency to 100 Hz (floats also work)  e.g. 100.5, 5.2
    # sleep(5)
    # p.stop()                # stop the PWM output
    # GPIO.cleanup()          # when your program exits, tidy up after yourself
    return

def testKlep():
    GPIO.setmode(GPIO.BCM)  # choose BCM or BOARD numbering schemes. I use BCM
    GPIO.setup(17, GPIO.OUT)# set GPIO 25 as an output. You can use any GPIO port
    GPIO.setup(6, GPIO.OUT)# set GPIO 25 as an output. You can use any GPIO port

    p = GPIO.PWM(17, 50)    # create an object p for PWM on port 25 at 50 Hertz
    p.start(100)

    # GPIO.output(17, GPIO.HIGH)
    GPIO.output(6, GPIO.LOW)
    sleep(4)
    # GPIO.output(17, GPIO.HIGH)
    GPIO.output(6, GPIO.HIGH)
    sleep(1)
    # GPIO.output(17, GPIO.HIGH)
    p.start(25)
    GPIO.output(6, GPIO.LOW)
    sleep(2)
    # GPIO.output(17, GPIO.HIGH)
    GPIO.output(6, GPIO.HIGH)
    sleep(2)
    # GPIO.output(17, GPIO.LOW)
    GPIO.output(6, GPIO.LOW)
    return

def knopPressedDetected(param):
    print "Knop pressed:"
    return

def klepOpenDetected(param):
    print "open:"
    return

def klepClosedDetected(param):
    print "closed:"
    return

def rotation_decode(Enc_A):
    global counter
    print "decode"
    sleep(0.002) # extra 2 mSec de-bounce time
    Switch_A = GPIO.input(Enc_A)
    Switch_B = GPIO.input(Enc_B)
    print str(Switch_B)
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
    # initKlepSensor()
    initKnopSensor()
    # testKlep()
    # testPWM()
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

