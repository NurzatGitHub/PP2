class Myclass:
    def  str(self,string):
        self.string = string
    def getstring(self):
        self.string = input()
    def printstring(self):
        print(self.string)

line = Myclass()
line.getstring()
line.printstring()