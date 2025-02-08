class Mystrin:
    def __init__(self):
        self.s = ""
    def getString(self):
        self.s = str(input("Print any string: "))
    def printString(self):
        print(self.s.upper())

sh = Mystrin()
sh.getString()
sh.printString()