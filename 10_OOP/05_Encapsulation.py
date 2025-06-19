class Bank:
    __balance = 100

    def __init__(self, amount):
        self.amount = amount 

    def deposit(self, amount):
        amount = amount + self.__balance 

    def withdraw(self, amount):
        amount = self.__balance - amount