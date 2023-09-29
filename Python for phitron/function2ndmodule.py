                                                #Introduction to python
                                       
                                       #Date 1st 1st module date: 17th june,2023
                                                     #Module 1.3:
                                          #Basic data type and variable in python

"""python no need to declare any data type for the variable so it was easy to handle and most easy language".
"""
# age = 45
# print(age)
# collusion = "substitute"
# print(collusion)
# is_signle = True
# print(is_signle)

# #to know the type of the variable
# is_single=True
# print(type(is_signle))
# is_singele="Fuck you"
# print(type(is_singele))

                                  #Module 1.4 Basic input and output typecasting
# #How to take input
# money = input("Give me money:")
# print("here is money:" ,money)

# # When we add some values and use input() function but 
# # that time it take as a string so we have to apply typecast  for
# # changing the data type. Here are some example

# firstmoney=input("Enter money 1: ")
# secondmoney=input("Enter money 2: ")
# first=int(firstmoney)
# second=int(secondmoney)
# total=first+second
# print("Total money:",total)




                                # python 2nd day 2nd module date sat, 27 may, 2023
                                                    # fucntion

"""
2.1 introduction to function in python
indentation means space it work as a bracket.

def is called define.
function likte gele def likte hoi
"""
# def double_it(num):
#     result=num*2
#     print(result)

# double_it(8)
# double_it(88)

# def sum(num1,num2):
#     result= num1+num2
#     return result
# total = sum(23,45)
# print(total)

"""
2.2 Default parameters and args in python


"""
# def sum(num1,num2,num3): 
#     # """this are called argument where the value add at the bracket"""
#     result= num1+num2+num3
#     return result
# total = sum(99,11,5) 
# # """this are called parameter where the value add at the bracket"""
# print('total:',total)

# """jodi parameter 2ta pataite hoi but argument 3ta rakte hoi
# tahole j parameter ta patabona shetak 0 diye assign korte hbe jemon
# num3=0
# """
# def sum(num1,num2,num3=0): 
#     # """this are called argument where the value add at the bracket"""
#     result= num1+num2+num3
#     return result
# total = sum(99,11) 
# # """this are called parameter where the value add at the bracket"""
# print('total:',total)

"""
If i need to add many number on the arguments but I dont no how many numbers
need to add there also I dont want to add num=0 repeatedly. That's why tupple are use.
Tupple is like one kind of array or list.

what is tupple?
A tuple is a data structure in programming that is used to store multiple elements together. 
It is an ordered collection of values, enclosed in parentheses and separated by commas. 
Tuples are similar to lists or Array, but they are immutable, meaning their elements cannot be modified once they are created.
Tuples can contain elements of different data types, such as integers, floats, strings, or even other tuples.

The procude for write tupple:
def all_sum(*numbers): //here adding (*) before the arguments are tupple
    print(numbers)

total = all_sum(12,23,5,7,8)
print(total)
"""


#                   #2.3 (advanced) kargs, multiple return from a function
# def func(a,b):
#     nul=f'showing the value: {a},{b}'
#     return nul

# nul=func(1,2)
# print(nul)

#                         #2.4 Local and global variable
# amount = 3000 #global variable
# def take_amount(item,taka):
#     #taka =2000 #local variabl
#     global amount #global  is a keyword use for accesing global variable
#     amount= amount-taka
#     print(f'Show the amount of the {item} ',amount)

# take_amount('Chocolate',1000)


#2.5 Module Built in function and import module
# def taka_dao(taka):
#     Fachis_dinme_paisa_double = 2*taka
#     print(f'Paisa hi paisa hoga now ap bare lok ho apki total amount:',Fachis_dinme_paisa_double)

# taka_dao(20000)

#fiie 2nd
# from function2ndmodule import taka_dao
# taka_dao(5000000)

# 2.6 list 
# #Normal indexing:
#        #0   1  2   3    4  5   6
# list =[10, 11, 12, 23, 45, 67, 8]
#        #-6  -5  -4  -3  -2  -1  0
# #printing value of index 0 to before 2 
# print(list[0:2])
# #printing value of index 1 to before 6 
# print(list[1:6])
# #python has the power of printing without mentioning the index. for example
# # if before and after of colon ':' has no value or given only one value it will automatically
# # produce the 1st or last index 
# print(list[:6])
# print(list[0:])
# print(list[:])
# print(list[1:6:2])
 
                                # Module 3.1
# If i want to write a name with single quotation
# like abdur's rahman then it will show a error
# thats why I have to use (/) 
# example: abdur\'s rahman

# name = 'anisul\'s islam' #this is call escaping
# name2= 'love'
# name3= """Sakiya tuj 
#         johor mumu"""
# print(name)
# print(name2)
# print(name3)

#string is a sequence of character
#list are called that means changeable and non-mutable means unchangeable
#string cant be change 
# for example:
# name2[0]='F'
# print(name2)
# this error will be show:
#  File "g:\Python for phitron\function2ndmodule.py", line 174, in <module>
#     name2[0]='F'
#     ~~~~~^^^
# TypeError: 'str' object does not support item assignment
# print(name2[2])#findout the value of input index
# print(name3[::-1])#string canbe reversable
# print(name3[1:6])#string can sliceable

                            
                            
                            # Moudle 3.2
#Tupple is one kind of list where many values are store
# #tupple cant be changeable like assigning any value
# print(len(name))
# item = ([0,2,6],[5,99,7],[4,7,991])
# print(item)
# #After changing the single value of the list of single tupple
# print("After changing the single value")
# item [0][1]= 45
# item [2][0]= 23
# print(item)

 # #Module 3.3 Set and set methods in python
# # Set is a unique item

"""         List --> []

            tupple --> ()
            
            set --> {}
"""
# numbers=[12,56,98,78,56,12,6,98]
# print(numbers)
# number_set=set(numbers)
# print(number_set)

# #number add
# number_set.add(47)
# print(number_set)

# #remove
# number_set.remove(6)
# print(number_set)

# len(number_set)

# A= {5,6,8,9}
# B= {10,6,9}
# print(A&B)
#  other things are on websites

            #Module-3.4 Dictionary and Dictionary methods in python
# Dictionary is like key value pair
# numbers = [12,56,98,78,56,12,26,98]
# person1 =['Anis', 'Kalipur', 23, 'student']
# # {key: valuem, key: value, key:value}
# person ={'name':'Anis', 'Address': 'Saltgola','Age': 23, 'Job':'Student'}
# print(person)
# print(person['Job'])
# # Dictionaries are mutable so I can change any of the value from the list or tuple
# print("Biyer age")
# person2 ={'Name':'Sakiya Tuj Johora', 'Address': 'Hulaine, Badamtol','Age': 22, 'Profession':'Amr Bou'}
# print(person2)
# print(person2['Profession'])
# print(person2.keys()) #for printing the keys of dictionaries
# print(person2.values())  #for printing the values of dictionaries

# print("Biyer Por")
# person2['Jamai']='Anis'
# print(person2)
# person2['Address']='Anis er bari'
# print(person2)

# other things are found on website

# import pyautogui
# from time import sleep
# sleep(10)

# pyautogui.write("bepar ta kintu moja onk", interval=0.01)
# pyautogui.press('enter',presses=1)




