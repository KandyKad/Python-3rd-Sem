class Shape:
    def __init__(self):
        self.area=0
    def print_area(self):
        print("Area is:",self.area)
class Square(Shape):
    def __init__(self,l):
        self.l=l
        self.area=self.l*self.l
    def print_area(self):
        print("Area is:",self.area)
a=Shape()
a.print_area()
b=Square(3)
b.print_area()
