
class ScreenInfo:
    outputListeners = []

    def __init__(self):
        pass

    def addOutputListener(self, listener):
        self.outputListeners.append(listener)

    def printScreen(self):
        for listener in self.outputListeners:
            listener.display("w: bbq:110 meat:43", 1);
            listener.display("s: bbq:115 meat:48", 2);
            listener.display("75% open, fan on", 4);
