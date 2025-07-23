
#input('What is your name--')                     # This is input function.

user_name = input('Enter your name - ')

print(f'welcome {user_name}')                     # To ask the input from user and print the message with addition using format 'f'. 

print('Programme to sum of two numbers')
num1 = int(input('Enter the first number - '))    # Here we are giving the "int" funtion to take the input as integers(numeric) but not a string.
num2 = int(input('Enter the second number - '))
result = num1 + num2
print(f'The sum of two numbers is - {result}')