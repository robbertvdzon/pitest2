import MenuController
import InputListener
from enum import Enum

# class MenuControllerImpl(MenuController, InputListener):

class MenuMode(Enum):
     IN_INFOSCREEN = 1
     IN_MAINMENU = 2
     IN_SUBMENU = 3

class MenuControllerImpl:
    outputListeners = []
    screenInfo = {}
    subMenus = []
    currentMenuNr = -1
    currentScreen = {}
    mode = MenuMode.IN_INFOSCREEN


    def __init__(self):
        pass

    def addSubMenu(self, subMenu):
        self.subMenus.append(subMenu)

    def addOutputListener(self, listener):
        self.outputListeners.append(listener)

    def buttonUp(self):
        if (self.mode == MenuMode.IN_INFOSCREEN):
            self.currentMenuNr = -1
            for listener in self.outputListeners:
                listener.clear()
        if (self.mode == MenuMode.IN_INFOSCREEN or self.mode == MenuMode.IN_MAINMENU):
            self.mode = MenuMode.IN_MAINMENU
            self.currentMenuNr = self.currentMenuNr+1
            if (self.currentMenuNr>=len(self.subMenus)):
                self.currentMenuNr =0

            self.currentScreen = self.subMenus[self.currentMenuNr]
            for listener in self.outputListeners:
                listener.display("MAIN MENU", 1)
                listener.display(self.currentScreen.getMenuName(), 2)
        elif  (self.mode == MenuMode.IN_SUBMENU):
            self.currentScreen.buttonUp()



    def buttonDown(self):
        if (self.mode == MenuMode.IN_INFOSCREEN):
            self.currentMenuNr = len(self.subMenus)
            for listener in self.outputListeners:
                listener.clear()
        if (self.mode == MenuMode.IN_INFOSCREEN or self.mode == MenuMode.IN_MAINMENU):
            self.mode = MenuMode.IN_MAINMENU
            self.currentMenuNr = self.currentMenuNr-1
            if (self.currentMenuNr<=-1):
                self.currentMenuNr =len(self.subMenus)-1
            self.currentScreen = self.subMenus[self.currentMenuNr]
            for listener in self.outputListeners:
                listener.display("MAIN MENU", 1)
                listener.display(self.currentScreen.getMenuName(), 2)
        elif  (self.mode == MenuMode.IN_SUBMENU):
            self.currentScreen.buttonDown()

    def buttonPressed(self):
        print "pressed"

        if (self.mode == MenuMode.IN_INFOSCREEN or self.mode == MenuMode.IN_MAINMENU):
            print "in menu of info"
            for listener in self.outputListeners:
                listener.clear()
            self.currentScreen.printScreen()
            self.mode = MenuMode.IN_SUBMENU
        elif  (self.mode == MenuMode.IN_SUBMENU):
            print "in submenu"
            self.currentScreen.buttonPressed()

    def openMainMenu(self):
        pass

    def closeMenu(self):
        print "close menu"
        self.mode = MenuMode.IN_INFOSCREEN
        for listener in self.outputListeners:
            listener.clear()
        self.screenInfo.printScreen()

    def nextMenu(self):
        pass

    def prevSetMenu(self):
        pass

    def startDisplay(self):
        self.screenInfo.printScreen()

    def setScreenInfo(self, screenInfo):
        self.screenInfo = screenInfo
