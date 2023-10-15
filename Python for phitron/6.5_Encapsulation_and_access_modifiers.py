class Bank:
    def __init__(self, holder_name, initial_deposit):
        self.holder_name=holder_name
        self.__balance=initial_deposit
    def deposit(self, amount):
        self.__balance +=amount
    
    def get_balance(self):
        return self.__balance

anis = Bank('anis',1000)
print(anis.holder_name)
anis.deposit(4000)
print(anis.get_balance())

ro dkte hbe