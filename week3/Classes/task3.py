class Shape:
    """This class print to default Area"""
    area = 0
    def defaultArea(self):
        print(self.area)
    class Square:
        """This subclass to Shape"""
        def __init__(self,length):
            self.length = length
        def Area(self):
            area = self.length**2
            print(area)

class Rectangle(Shape):
    """class named Rectangle which inherits from Shape"""
    def __init__(self,width):
        self.width = width
    def Area2(self):
        print(self.width * self.Square(5).length)

Sh1 = Shape()

Sh1.defaultArea()

Sh1.Square(5).Area()

Sh2 = Rectangle(3)

Sh2.Area2()