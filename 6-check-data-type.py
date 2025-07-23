
#The below code throughs an error because we are using a number (num2=20) as a string. So it throws an error while executing.
num1=10
num2='20' 
price=2.5
boolean=True
#print(num1 + num2)

'''
output is like below
➜  python python3 6-check-data-type.py
<class 'int'>
<class 'str'>
'''





#To overcome this error we use type in the print to state which type of data it is.
print(type(num1))
print(type(num2))
print(type(price))
print(type(boolean))
'''
output is like below
➜  python python3 6-check-data-type.py
<class 'int'>
<class 'str'>
<class 'float'>
<class 'bool'>
'''