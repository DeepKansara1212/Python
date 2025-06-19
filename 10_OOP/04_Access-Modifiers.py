class Animal:
    # Public Attributes
    name1 = "lion"


class Birds:
    # Protected Attributes
    _name2 = "Sparrow"

    # Private Attributes
    __age = 5
    print(__age)

obj1 = Animal()
print(obj1.name1) 

obj2 = Birds()
print(obj2._name2) 
print(obj2.__age)