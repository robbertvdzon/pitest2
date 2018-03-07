from display import *
import I2C_LCD_driver
import Adafruit_ADS1x15
import RPi.GPIO as GPIO
from time import *

KlepSensorPinOpen = 22
KlepSensorPinClosed = 27

def initMotor():
    initKlepSensor()
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(5, GPIO.OUT) # FAN
    GPIO.output(5, GPIO.HIGH)
    sleep(2)
    GPIO.output(5, GPIO.LOW)


    GPIO.setup(12, GPIO.OUT) # aan / uit
    GPIO.setup(17, GPIO.OUT) # richting
    GPIO.output(12, GPIO.HIGH)

    GPIO.output(17, GPIO.HIGH)
    sleep(2)
    GPIO.output(17, GPIO.LOW)
    sleep(2)
    GPIO.output(17, GPIO.HIGH)
    sleep(2)
    GPIO.output(17, GPIO.LOW)
    sleep(2)
    GPIO.output(12, GPIO.LOW)


    # GPIO.output(5, GPIO.LOW)
    # sleep(1)
    # GPIO.output(5, GPIO.HIGH)

    # p = GPIO.PWM(12, 50)    # create an object p for PWM on port 25 at 50 Hertz
    # p.start(80)
    # # sleep(2)
    # GPIO.output(17, GPIO.LOW)
    # sleep(2)
    # # p.start(30)
    # GPIO.output(17, GPIO.HIGH)
    # sleep(2)
    # GPIO.output(17, GPIO.LOW)
    # sleep(2)
    # GPIO.output(17, GPIO.HIGH)
    # GPIO.output(12, GPIO.LOW)

    print '-----------------'
    while True:
        p1 = GPIO.input(22)
        p2 = GPIO.input(27)
        print('p1='+str(p1))
        print('p2='+str(p2))
        # Pause for half a second.
        sleep(0.5)

    return


def initKlepSensor():
    print "Klep sensor init"
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(KlepSensorPinOpen, GPIO.IN) # pull-ups are too weak, they introduce noise
    GPIO.setup(KlepSensorPinClosed, GPIO.IN)
    GPIO.add_event_detect(KlepSensorPinOpen, GPIO.RISING, callback=klepOpenDetected, bouncetime=500) # bouncetime in mSec
    GPIO.add_event_detect(KlepSensorPinClosed, GPIO.RISING, callback=klepClosedDetected, bouncetime=500) # bouncetime in mSec
    # sleep(10)
    return


def klepOpenDetected(param):
    p1 = GPIO.input(22)
    p2 = GPIO.input(27)
    print('p1='+str(p1))
    print('p2='+str(p2))

    # p2 = GPIO.input(27)
    if (p2==1):
        print "open:"
    return

def klepClosedDetected(param):
    p1 = GPIO.input(22)
    p2 = GPIO.input(27)
    print('p1='+str(p1))
    print('p2='+str(p2))
    # p1 = GPIO.input(22)
    if (p1==1):
        print "closed:"
    return
