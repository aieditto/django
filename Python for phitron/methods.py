# def function():
#     print('calling someone i dont know')
#     return 'call done'
# class phone:
#     price = 1200
#     color= 'yellow'
#     brand='sandy'
#     features=['camera', 'speaker']
    
#     def call(self): 
#         # self is use for calling the method in class
#         print('calling one person')
    
#     def send_sms(self, xhone, message):
#         text= f'send message to {xhone} and sms {message}'
#         return text

# amar_phone= phone()
# print(amar_phone.features)

# busy= amar_phone.call()
# result= amar_phone.send_sms(233, 'Inky pinky ponky')
# print(result)

class Calculator:
    brand= 'Casio 6251'
    def add(self, num1, num2):
        result= num1+num2
        return result
    def sub(self, num1, num2):
        result2= num1-num2
        return result2

addition=Calculator()
print(addition.brand)
result=addition.add(55,5)
print(result)

result2=addition.sub(5,2)
print(result2)
