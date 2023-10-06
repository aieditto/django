# class Bank:
#     def __init__(self, balance):
#         self.balance=balance
#         self.min_withdraw=100
#         self.max_withdraw=10000
    
#     def get_balance(self):
#         return self.balance
    
#     def deposit(self, amount):
#         if amount> 0:
#             self.balance += amount
#             print(f'your balance is{self.balance}')
    
#     def withdraw(self,amount):
#         if amount<self.min_withdraw:
#             print(f'Sorry. Minimum withdraw is{self.min_withdraw}')
#         elif amount>self.max_withdraw:
#             print(f'Sorry. Maximum withdraw is {self.max_withdraw}')
#         else:
#             self.balance-=amount
#             print(f'Your Balance {self.get_balance()}')   

# dbl=Bank(5000)
# dbl.withdraw(101)

class Exam:
    
    def __init__(self, person, marks):
        self.person=person
        self.marks=marks
        print(f'student name{self.person}')
        self.minimum_marks=33
    
    # def max(self):
        
    
    def result(self, marks):
        if self.marks>90:
            print(f'you got A+ your marks {self.marks}')
        elif self.marks>= 80 & self.marks<=89:
            print(f'you got A your marks {self.marks}')
        elif self.marks>= 70 & self.marks<=79:
            print(f'you got B+ your marks {self.marks}')
        elif self.marks>= 60 & self.marks<=69:
            print(f'you got C your marks {self.marks}')
        elif self.marks<self.minimum_marks:
            print(f'you are failed and your result {self.marks}')

Student = Exam('Anis', 3)
Student.result(60)

