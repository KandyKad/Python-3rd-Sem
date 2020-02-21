import math
class Rect():

    def __init__(self,l,b):
        self.l = l
        self.b = b

    def area(self):
        return (self.l*self.b)

recta = Rect(float(input("Enter the length: ")),float(input("Enter the breadth: ")))
print("Area of the rectangle is: ")
print(recta.area(),"sq. units.")
