# print(10 + 25)
# print("10" + 25)
# print("10" + "25") 


class Shape:
    def area(self):
        return "Undefined"
    
class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__()
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width 
    
class Circle(Shape):
    def __init__(self, radius):
        super().__init__()
        self.radius = radius

    def area(self):
        import math
        return math.pi * self.radius ** 2
    

recatangle1 = Rectangle(10,20)
result = recatangle1.area()
print(result) 

circle = Circle(2)
print(circle.area()) 

shape = Shape()
print(shape.area()) 