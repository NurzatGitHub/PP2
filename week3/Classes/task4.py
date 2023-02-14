import math

class Point():
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def show(self):
        print(self.x,self.y,sep = ':')
    def move(self):
        x1 = int(input('move to change these coordinates x: '))
        y1 = int(input('move to change these coordinates y: '))
        self.x += x1
        self.y += y1
        print(self.x,self.y,sep = ':')
    def dist(self):
        d = math.sqrt(self.x**2 + self.y**2)
        print('the distance between 2 points: ',d)

P = Point(4,5)
P.show()
P.move()
P.dist()