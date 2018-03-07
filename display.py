import I2C_LCD_driver

class Display:

    def __init__(self):
        self.initDisplay()

    def onMessage(self, event, message):
        if (event=="display"):
            self.writeDisplay(message,2)
        print 'got message in display: '+event+' '+message

    def display(self, text, regelnr):
        self.writeDisplay(text,regelnr)

    def clear(self):
        self.clearDisplay()

    def initDisplay(self):
        global mylcd
        mylcd = I2C_LCD_driver.lcd()
        mylcd.lcd_display_string("Smoker test", 1)
        return

    def writeDisplay(self, text, line):
        global mylcd
        mylcd.lcd_display_string(text, line)

    def clearDisplay(self):
        global mylcd
        mylcd.lcd_display_string("                    ", 1)
        mylcd.lcd_display_string("                    ", 2)
        mylcd.lcd_display_string("                    ", 3)
        mylcd.lcd_display_string("                    ", 4)
