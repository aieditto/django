# # #based class, parent class/ Inheritance
# # # derived class, child class,

# # """This Device class are the common class or parent class and the other class
# #     are child class. So child class can inherit the parent class. So, If we need something from the parent class we can access.
# #     It was very helpful for not repeating code and less time complexity.
# # """
# # class Device:
# #     def __init__(self, brand, price,color, origin):
# #         self.brand=brand
# #         self.price=price
# #         self.color=color
# #         self.color=origin
        
# #     def __init__(self,memory):
       
# #         self.memory=memory
    
# #     def run(self):
# #         return f'Running Laptop: {self.brand}'
    
# #     def coding(self):
# #         return f'learning python and practicing'
    
    
# # class Phone:
# #     def __init__(self, dual_sim):
    
# #         self.dual_sim = dual_sim

# #     def phone_call(self, number,text):
# #         return f'send sms to: {number} with: {text}'

# # class Camera:
# #     def __init__(self, pixel):
        
# #         self.pixel=pixel
    
# #     def change_lens(self):
# #         pass



# """Another Example"""
# class Vehicle:
#     def __init__(self, name,  price):
#         self.name=name
#         self.price=price
    
#     def __repr__(self) -> str:
#         return f'Vechile Name: {self.name}, price{self.price}'
    
#     def move(self):
#         pass
# class Bus(Vehicle):
#     def __init__(self, name, price, seat):
#         self.seat=seat
#         super().__init__(name, price)
    
#     def __repr__(self) -> str:
#         return super().__repr__()

# class Truck(Vehicle):
#     def __init__(self, name, price, weight):
#         self.weight=weight
#         super().__init__(name, price)

# class Picktup(Truck):
#     def __init__(self, name, price, weight):
#         super().__init__(name, price, weight)

# class ACBus(Bus):
#     def __init__(self, name, price, seat,temparature):
#         self.temparature=temparature
#         super().__init__(name, price, seat)
#     def __repr__(self) -> str:
#         return f'Vehicle Name: {self.name}, vehicle price: {self.price}, total seat {self.seat}, temparature {self.temparature}'

# Green_line=ACBus('Greeen', 10000000, 40, 21)
# print(Green_line)


"""Example 3 multi level inheritance"""
class Batch:
    def __init__(self,section):
        self.section=section
    
    def __repr__(self) -> str:
        pass

class Section(Batch):
    def __init__(self, section, ID):
        self.ID=ID
        super().__init__(section)

class ID(Section):
    def __init__(self, section, ID, name):
        self.name=name
        super().__init__(section, ID)

class Student(ID):
    def __init__(self, section, ID, name, Weight, Height, Age):
        self.Weight=Weight
        self.Height=Height
        self.Age=Age
        super().__init__(section, ID, name)
    
    def __repr__(self) -> str:
        return f'Section {self.section}, Id: {self.ID}, Name: {self.name}, Weight: {self.Weight},Height: {self.Height}, Age: {self.Age}'

Anis = Student('B', 220238063, 'Md Anisul Islam', 75, '5\'7', 23)
print(Anis)