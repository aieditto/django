from abc import ABC, abstractclassmethod #abstract class importing
class Animal(ABC): #abstract method calling  ABC mean Abstract Base Class
    @abstractclassmethod #abstractmethod use for identifying which method is need to abstract
    def eat(self):
        pass
    @abstractclassmethod 
    def move(self):
        pass

class Anis(Animal):
    def __init__(self, name) -> None:
        self.category='Anisul'
        self.name=name
        super().__init__()
    def eat(self):
        print('from eat method')
    
    def move(self):
        print('Khaifa Halek')

Anisul=Anis('Khana dao')
Anisul.eat()
Anisul.move()

""""@abstractclassmethod is the process or way where you can from django.conf import settings
a sub class to create the same method which are already on  parent class method.  
"""