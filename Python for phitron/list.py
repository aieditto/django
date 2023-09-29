#Normal indexing:
       #0   1  2   3    4  5   6
list =[10, 11, 12, 23, 45, 67, 8]
       #-6  -5  -4  -3  -2  -1  0
#printing value of index 0 to before 2 
print(list[0:2])
#printing value of index 1 to before 6 
print(list[1:6])
#python has the power of printing without mentioning the index. for example
# if before and after of colon ':' has no value or given only one value it will automatically
# produce the 1st or last index 
print(list[:6])
print(list[0:])
print(list[:])
print(list[1:6:2])
 
#Module 2.7
numbers =[10,2,34,5,6]
numbers.append(7)
print(numbers)
numbers.insert(1,55)
print(numbers)