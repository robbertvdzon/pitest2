class EventBus:
    global listeners
    listeners = []
    def emit(self, event, message):
        global listeners
        for i in listeners:
            i.onMessage(event, message)
        return

    def register(self, listener):
        global listeners
        listeners.append(listener)
        return


def initEventBus():
    global bus
    bus = EventBus()
    return

def getEventbus():
    global bus
    return bus
