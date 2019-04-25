import math

class StackError(Exception): pass
class InvalidInputError(StackError): pass

class Circle:

    def __init__(self , x=0, y=0, radius=1):
        self.x = x
        self.y = y
        self.radius = radius
    
    def setRadius(self, val):
        if val <= 0:
            raise InvalidInputError
        else:
            self.radius = float(val)

    def getArea(self):
        area = math.pi * (self.radius) ** 2
        return area 

    def getPerimeter(self) :
        return 2 * math.pi * self.radius

    def move(self, x , y):
            self.x = x
            self.y = y
            return x, y

    def getX(self):
        return self.x
        
    def getY(self):
        return self.y



        
