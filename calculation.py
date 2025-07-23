#Here we are creating functions for calculations to use this file as a module in another 19th programme.

def add(num1,num2):
    return num1 + num2 

def sub(num1,num2):
    return num1 - num2

def mul(num1,num2):
    return num1 * num2

def even_or_odd (num):
    if num % 2 == 0:
        print('Number is even')
    else:
        print('Number is odd')


#calling the function. We should not call this function in the same script, bcz it will also print this output in 19th script.
# even_or_odd (50)