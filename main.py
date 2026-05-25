#6-m
class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance
        
    @property
    def balance(self):
        return self.__balance
    
    @balance.setter
    def balance(self, new_balance):
        self.__balance = new_balance
        
b1 = BankAccount("<NAME>", 10000)
print(b1.name)

res = b1.balance
print(res)

b1.name = "<NAME>"
print(b1.name)
