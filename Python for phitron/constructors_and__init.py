# class Phone:
#     manufacture ='China'
    
#     def __init__(self, owner, brand,price):
#         self.owner=owner
#         self.brand=brand
#         self.price=price
        
#         # __init__ mean initialize which are use as constructor
        
#     def send_msg(self, phone, sems):
#         text= f'sending to: {phone} {sems}'
#         print(text)
    

# my_phone= Phone('Anis', 'tecno', '8500')
# print(my_phone.owner, my_phone.brand, my_phone.price)

class Phone:
    
    def __init__(self, num1, num2):
        self.num1=num1
        self.num2=num2
        
addition=Phone(10,19)
result=addition.num1+addition.num2
print(f'{addition.num1} + {addition.num2} = {result}')

sub=Phone(14,5)
result2=sub.num1-sub.num2
print(f'{sub.num1} - {sub.num2} = {result2}')