class Shape:
    """This class print to default Area"""
    area = 0
    def Area(self):
        print(self.area)
    class Square:
        """This subclass to Shape"""
        def __init__(self,length):
            self.length = length
        def Area(self):
            area = self.length**2
            print(area)
Sh1 = Shape()

Sh1.Area()
Sh1.Square(5).Area()
