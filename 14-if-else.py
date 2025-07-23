
# This is if, else condition.
if True:
    print('This is True')
else:
    print('This is False')
    
    
    
# Here we are adding conditions and checking the if,else condition.   
if 20>30:
    print('This is True')
else:
    print('This is false')
    
    
# Example-1 
print('Enter a number to check if the number is Even number or not')
num = int(input('Enter a number - '))

if num % 2 == 0:
    print('This number is Even number')
else:
    print('The given number is not Even number')
    
    
    
# Example-2
Users = ('Srikanth','nainika','Lasya')
if 'Nainika' in Users:                      #To check whether the user is present in the list or not.We can also use only 'if' condition. It is not compulsory to use 'else'.
    print('User exists in the list')
else:
    print('User does not exists in the list')
    

# Example-3 To find whether the given list is empty or not.
users = ('sri','lasya')
if users:
    print('The list is not empty')
else:
    print('The list is empty')
    
    
    
# Example-4 To use multiple condition by using "elif"
marks = int(input('Enter the total number of marks - '))
if marks >=80:
    print('A Grade')
elif marks >=60:
    print('B Grade')
elif marks >=40:
    print('C Grade')
else:
    print('FAILED...!')
    
    
# Example-5 if-else NESTING
age = 20
voter_id = False

if age >= 18:
    if voter_id:
        print('You can vote')
    else:
        print('Please apply for the voter ID first')
else:
    print('You cannot vote')
    
    

# Example-6 Logical Operators "and" , "or". In the shell scripting we use this as '&&' , '||'
age = 20
voter_id = False

if age >=18 and voter_id:
    print('You can vote')
else:
    print('You cannot vote')
    
    
# Example-7 In the same way you can use 'or' operator where one condition is true.