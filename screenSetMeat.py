
class ScreenSetMeat:
    outputListeners = []
    tempSet = 110
    menuController = {}

    def __init__(self):
        pass

    def getMenuName(self):
        return "Set Meat temp"

    def setMenuController(self, menuController):
        self.menuController = menuController

    def addOutputListener(self, listener):
        self.outputListeners.append(listener)

    def buttonUp(self):
        self.tempSet = self.tempSet+1
        self.printScreen()

    def buttonDown(self):
        self.tempSet = self.tempSet-1
        self.printScreen()

    def buttonPressed(self):
        self.menuController.closeMenu()

    def printScreen(self):
        for listener in self.outputListeners:
            listener.display("Set Meat temp:", 1);
            listener.display(str(self.tempSet)+" deg", 2);
