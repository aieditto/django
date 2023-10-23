# """
#     1. Read only ----> you cannot set the value. value cannot be changed.
#     2. getter --> get a value of a property. Most of the time you will get the value of a privete attribute.
#     3. setter---> set a value of a property through a method, Most of the time, you will set the value of a private property.
# """
# class User:
#     def __init__(self, name, age, money ) -> None:
#         self._name=name #protected variable
#         self._age=age #protected variable
#         self.__money= money #private variable
#     @property #this is getter property by default read only attribute.
#     def age(self):
#         return self._age
    
#     @property
#     def salary(self):
#         return self.__money
    
#     @salary.setter  #this is "setter" attribute. For setting setter attribute first you have to mention the method name which have to set setter that .setter
#     def salary(self, value):
#         if value<0:
#             return f'you have not enough money!'
        
#         else: 
#              self.__money+=value
        
    
# samsu = User('Anis', 23, 12000)

# # print(samsu.__money)
# #print(samsu.age()) 
# """now this age is behaving like method 
# but if we need to call it like a attribute than we can use 
# ""  @property ""  upon on that method
# """
# print(samsu.age) 
# print(samsu.salary)
# samsu.salary=500
# print(samsu.salary)

class User:
    def __init__(self, name, age, money) -> None:
        self._name=name
        self._age=age
        self.__money=money
    @property
    def age(self):
        return self._age
    
    @property
    def salary(self):
        return self.__money
    
    @salary.setter
    def salary(self, value):
        if value<0:
            return f'Ami Fokir'
        else:
            self.__money+=value

Anis= User('Anis', 23, 12000)
print(Anis.age)
print(Anis.salary)
Anis.salary=1200
print(Anis.salary)
