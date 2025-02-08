import math
class Point():
    def __init__(self, x, y ):
        self.x = x
        self.y = y
    def show(self):
        print(f"Poitn({self.x},{self.y})")
    def move(self,n_x,n_y):
        self.x = n_x
        self.y = n_y
    def dist(self,other):
        return math.sqrt((self.x**2-other.x**2)+(self.y**2-other.y**2))
p1 = Point(1, 2)
p1.show()
p2 = Point(6,7)
p1.move(4,5)
p1.show()
print("Distance:", p2.dist(p1))