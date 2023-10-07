#based class, parent class/ Inheritance
# derived class, child class,

"""This Device class are the common class or parent class and the other class
    are child class. So child class can inherit the parent class. So, If we need something from the parent class we can access.
    It was very helpful for not repeating code and less time complexity.
"""
class Device:
    def __init__(self, brand, price,color, origin):
        self.brand=brand
        self.price=price
        self.color=color
        self.color=origin
        
    def __init__(self,memory):
       
        self.memory=memory
    
    def run(self):
        return f'Running Laptop: {self.brand}'
    
    def coding(self):
        return f'learning python and practicing'
    
    
class Phone:
    def __init__(self, dual_sim):
    
        self.dual_sim = dual_sim

    def phone_call(self, number,text):
        return f'send sms to: {number} with: {text}'

class Camera:
    def __init__(self, pixel):
        
        self.pixel=pixel
    
    def change_lens(self):
        pass