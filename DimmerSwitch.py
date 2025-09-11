class DimmerSwitch():
    def __init__(self):
        self.switchIsOn = False
        self.brightness = 0
    def turnOn(self):
        self.switchIsOn = True
    def turnOff(self):
        self.switchIsOn = False
    def raiseLevel(self):
        if self.brightness < 10:
            self.brightness += 1
    def lowerLevel(self):
        if self.brightness > 0:
            self.brightness -= 1
    def show(self):
        print(self.switchIsOn)
        print(self.brightness)
def main():
    d0 = DimmerSwitch()
    d0.show()
    d0.turnOn()
    for counter in range(20):
        d0.raiseLevel()
    d0.show()
    for counter in range(20, 0, -1):
        d0.lowerLevel()
    d0.show()
main()