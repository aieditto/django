# Inheritance and composition are two fundamental concepts in object-oriented programming that allow you to design and structure your code. They serve different purposes and have their own advantages and use cases. Let's explore both concepts:
# Inheritance:

#     Inheritance is an "is-a" relationship where one class derives properties and behaviors from another class. It allows you to create a new class based on an existing class, inheriting its attributes and methods.
#     The new class (subclass or derived class) can extend or modify the behavior of the existing class (base class or superclass) and also add its own attributes and methods.
#     Inheritance promotes code reusability by allowing you to use and build upon existing classes. It can help you model hierarchies and relationships between objects.
#     However, it can lead to tight coupling between classes, making the code harder to maintain and less flexible, especially if the inheritance hierarchy becomes deep and complex.

# Example:

# python

# class Vehicle:
#     def __init__(self, wheels):
#         self.wheels = wheels

# class Car(Vehicle):
#     def __init__(self, wheels, brand):
#         super().__init__(wheels)
#         self.brand = brand

# Composition:

#     Composition is a "has-a" relationship that allows you to create complex objects by combining and using instances of other classes. It involves creating objects of one class within another class.
#     Composition promotes flexibility and loose coupling, as you can change the behavior of a class by swapping out its components without affecting the entire class.
#     It's often more suitable when you need to build complex systems with reusable components. Composition is favored over inheritance when designing for flexibility and maintainability.

# Example:

# python

#     class Engine:
#         def start(self):
#             print("Engine started")

#     class Car:
#         def __init__(self):
#             self.engine = Engine()

#         def drive(self):
#             print("Driving the car")
#             self.engine.start()

# In summary, the choice between inheritance and composition depends on your design goals. If you want to create a hierarchy of closely related classes with shared characteristics, inheritance can be appropriate. If you want to build flexible, maintainable, and loosely coupled systems, composition is often a better choice. In practice, a combination of both inheritance and composition is frequently used to achieve the desired design and code structure.

# other example: https://www.geeksforgeeks.org/inheritance-and-composition-in-python/


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

#Other way:
# # Define the values you want to set for CPU cores, RAM size, and hard drive capacity
# core_count = 4  # Number of CPU cores
# ram_size_gb = 16  # RAM size in gigabytes
# hd_capacity_gb = 512  # Hard drive capacity in gigabytes

# # Create a Computer object with the specified values
# my_computer = Computer(core_count, ram_size_gb, hd_capacity_gb)

# # Access the components of the computer
# print("CPU Cores:", my_computer.cpu.core)
# print("RAM Size (GB):", my_computer.ram.size)
# print("Hard Drive Capacity (GB):", my_computer.hard_disc.capacity)
