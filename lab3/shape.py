class Shape:
    def area(self):
        return 0
class Square(Shape):
    def __init__(self,lenght):
        self.lenght = lenght
    def area(self):
        return self.lenght**2
sq = Square(4)
print(sq.area())

class Rectangle(Shape):
    def __init__(self,lenght, width):
        self.lenght = lenght
        self.width = width
    def area(self):
        return self.lenght * self.width
rc = Rectangle(4,5)
print(rc.area())
