# Class Attribute VS Instance Attribute

class Shop:
    cart=[] #list declare class attribute this for all not in function
    def __init__(self,buyer): #init funciton for construction
        self.buyer = buyer #attribute declare
        
    def add_to_cart(self, item):
        self.cart.append(item)

customer = Shop('Anisul Islam')
customer.add_to_cart('Audi')
customer.add_to_cart('Ferari')
customer.add_to_cart('Marcedies')
print(customer.cart)

customer2 = Shop('Anisul Islam')
customer2.add_to_cart('Audi')
customer2.add_to_cart('Ferari')
customer2.add_to_cart('Marcedies')
print(customer2.cart)


class Shop:
     
    def __init__(self,buyer): #init funciton for construction
        self.buyer = buyer #attribute declare
        self.cart=[] #instant attribute #list declare  this for all not in function
        
    def add_to_cart(self, item):
        self.cart.append(item)

customer = Shop('Anisul Islam')
customer.add_to_cart('Audi')
customer.add_to_cart('Ferari')
customer.add_to_cart('Marcedies')
print(customer.cart)

customer2 = Shop('Sakiya Islam')
customer2.add_to_cart('Lipstick')
customer2.add_to_cart('Eyeliner')
customer2.add_to_cart('Brush')
print(customer2.cart)