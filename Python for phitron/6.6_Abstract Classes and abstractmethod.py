class Animal:
    def eat(self):
        print('eating')
    def move(self):
        pass

class Monkey(Animal):
    def __init__(self,name) -> None:
        self.category='Monkey'
        self.name=name
        super().__init__()

layka = Monkey("lucky")
layka.eat()
