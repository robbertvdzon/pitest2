from display import *
from time import *

class Menu:
    def onMessage(self, event, message):
        print 'got message in menu: '+event+' '+message

def initMenu():
    global bus
    global menu
    menu = Menu()
    bus = getEventbus()
    print "call register:"
    bus.register(menu)
    print "Init menu:"
    return

def startMenu():
    print('Hello')
    bus.emit('test','message')
    bus.emit('display','START')
    print('Done')
    # try:
    #     whenile True:
            # writeDisplay("bla",4)
            # 4sleep(0.5)
# except KeyboardInterrupt: # Ctrl-C to terminate the program
