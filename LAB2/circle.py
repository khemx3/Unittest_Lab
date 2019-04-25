import math
class Circle:
    def __init__(self , x=0, y=0, radius):
        self.x = x
        self.y = y
        self.radius = radius
    
    def getArea(self):
        area = math.pi * (self.radius) ** 2
        return area 
    def getPerimeter(self) :
        return 2 * math.pi * self.radius
    def move(self, x , y):
        self.x = x
        self.y = y
        return x, y
