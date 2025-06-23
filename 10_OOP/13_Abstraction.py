from abc import ABC, abstractmethod

class Abstract(ABC):
    name = "Abstract"

    @abstractmethod
    def perimeter(self):
        return 4*self.length


    @abstractmethod
    def area(self):
        return self.length ** 2


class Square(Abstract):

    def __init__(self, length):
        self.length = length

    def perimeter(self):
        return super().perimeter()

    def area(self):
        return super().area()
    

obj = Square(5) 
print(obj.area())
print(obj.perimeter()) 