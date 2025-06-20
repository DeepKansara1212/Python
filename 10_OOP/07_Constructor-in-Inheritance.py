class Factory:
    def __init__(self, material, pockets):
        # Instance Attributes
        self.material = material
        self.pockets = pockets

    # Instance Method
    def show(self):
        print(f"The material is {self.material} & it has {self.pockets} no. of pockets")

class PuneFactory(Factory):
    def __init__(self, material, pockets, zips):
        super().__init__(material, pockets) 
        self.zips = zips

    def show2(self):
        print(f"The material is {self.material} & it has {self.pockets} no. of pockets & No. of zips are {self.zips}")


obj1 = Factory("cotton", 2) 
obj1.show()

obj2 = PuneFactory("asd", 25, 10)
obj2.show2() 