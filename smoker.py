from menu import *
from encoder import *
from display import *
from tempsensors import *
from motor import *
from MenuControllerImpl import *
from screenInfo import *
from screenSetBbq import *
from screenSetMeat import *


# initMotor()
# initTempSensors()
encoder = Encoder()
display = Display()
menuController = MenuControllerImpl()
# screens
screenInfo = ScreenInfo()
screenSetBbq = ScreenSetBbq()
screenSetMeat = ScreenSetMeat()

#----------- wiring
encoder.addInputListener(menuController)
menuController.addOutputListener(display)
screenInfo.addOutputListener(display)
screenSetBbq.addOutputListener(display)
screenSetBbq.setMenuController(menuController)
screenSetMeat.addOutputListener(display)
screenSetMeat.setMenuController(menuController)
menuController.setScreenInfo(screenInfo)
menuController.addSubMenu(screenSetBbq)
menuController.addSubMenu(screenSetMeat)

#--- start app
menuController.startDisplay()

# initMenu()

# writeDisplay("menu",2)
# startMenu()


try:
    while True:
        sleep(0.5)
except KeyboardInterrupt: # Ctrl-C to terminate the program
    GPIO.cleanup()
