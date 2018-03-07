from menu import *
from encoder import *
from display import *
from tempsensors import *
from motor import *


# initMotor()
initTempSensors()
initEventBus()
initDisplay()
initEncoder()
initMenu()

# writeDisplay("menu",2)
# startMenu()


try:
    while True:
        sleep(0.5)
except KeyboardInterrupt: # Ctrl-C to terminate the program
    GPIO.cleanup()
