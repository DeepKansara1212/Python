class Vehicle:
    def __init__(self, name, price):
        # print(self)
        self.name = name
        self.price = price

    def show(self):
        print(f"The name of vehicle is {self.name} & its price is {self.price}")


car = Vehicle("BMW", 10000000) 
car1 = Vehicle("Ford", 50000)  


# print(car.name)  
# print(car.price)

car.show() 
car1.show()
