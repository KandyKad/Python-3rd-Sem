import math
class Circle():

    def __init__(self,cir):
        self.cir = cir

    def area(self):
        return (math.pi*((self.cir)**2))

obj = Circle(int(input("Enter the radius of the circle: ")))
print("The Area of the circle is: ")
print(obj.area(),"sq. units.")
