# class Animal:
#     pass

# """"Inheritance provides you is a relation

#     composition:
# """
# #Dog is an animal
# class Dog(Animal):
#     pass
# #Dog is an animal
# class Tiger(Animal):
#     pass

# class Furniture:
#     pass

# #chair is a furniture
# class Chair(Furniture):
#     pass

# class Table(Furniture):
#     pass


# """Composition"""
# #Example for compostition
# class Engine:
#     def __init__(self) -> None:
#         pass
    
#     def start(self):
#         return "Engine Started"


# class Driver:
#     def __init__(self) -> None:
#         pass
    
# class Car:
#     def __init__(self) -> None:
#         self.engine=Engine()
#         self.driver=Driver()
    
#     def start(self):
#         self.engine.start()

class CPU:
    def __init__(self, core) -> None:
        self.core=core

class RAM:
    def __init__(self, size) -> None:
        self.size=size

class HardDrive:
    def __init__(self, capacity) -> None:
        self.capacity=capacity

class Computer:
    def __init__(self, core, ram_size, hd_capacity) -> None:
        self.cpu=CPU(core)
        self.ram=RAM(ram_size)
        self.hard_disc=HardDrive(hd_capacity)
        
mac=Computer(4,8,512)
print( f'The cpu size is {mac.cpu.core}, Hard Disk:{mac.hard_disc.capacity} Ram size: {mac.ram.size}')

