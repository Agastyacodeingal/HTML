class iostring:
    def __init__(self):
        self.name = ""
    def gestr(self):
        n = input("Enter your name")
        self.name = n
        self.name = self.name.upper()
    def printname (self):
        print("The given name when put in capital is ",self.name)
s1 = iostring()
s1.gestr()
s1.printname()