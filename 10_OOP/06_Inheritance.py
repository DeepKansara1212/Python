
# PARENT CLASS / SUPER CLASS
class Factory:
    def __init__(self, material, pockets):
        self.material = material
        self.pockets = pockets

    # Instance Method
    def show(self):
        print(f"The material is {self.material} & it has {self.pockets} no. of pockets")


# CHILD / SUB CLASS
class PuneFactory(Factory):
    pass 


obj1 = Factory("cotton", 2) 
obj1.show()

obj2 = PuneFactory("asd", 25)
obj2.show() 