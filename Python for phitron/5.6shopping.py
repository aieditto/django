"""Shopping Cart System"""

class Shopping:
    
    def __init__(self, name):
        self.name = name
        self.cart =[] #this is a list
    
    def add_to_cart(self, item, price, quantity):
        product={'item':item, 'price':price, 'quantity':quantity} #this is dictionary
        self.cart.append(product)
    
    def checkout(self, amount):
        total = 0
        print('Your Listed Item:')
        for item in self.cart:
            print(item)
            total += item ['price'] * item ['quantity']
        print('Your Total bill',total)
        
        if total>amount:
            print(f'Sorry! you have to pay {total-amount} more')
        else:
            extra= amount-total
            print(f'Your cash return', extra)
            

Anis = Shopping('Anisul Islam')
Anis.add_to_cart('Alu', 60, 9)
Anis.add_to_cart('Kodu', 30, 5)
Anis.add_to_cart('Letus', 300, 1)

# print(Anis.cart)
Anis.checkout(991)