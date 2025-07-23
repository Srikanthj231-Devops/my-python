# #Creating a funtion
# def greetings (user_name, age=None):            #define a variable for user-names and age. This will print the messages with user-names.
#     print('')
#     print('*'*35)
#     print(f'...........Welcome {user_name}...........')
#     print(f'Age is {age}')
#     print('....Thank you for signing in......')
#     print('*'*35)
#     print('')
    

# #Calling a function
# greetings ('Srikanth', 30)
# greetings ('Nainika', 4)
# greetings ('Lasya')          # Here we did not pass age in the function, but while creating the fun above we gave value as None. So this will print the age as None.




# #For example if we have to privide multiple variable in a function eg:hobbies, below is the programme.
# #This is dynamic arguments in functions....
# def greet(name, *hobbies):
#     print(f' Welcome {name}')
#     for hobby in hobbies:          #Here we are using Tuples.
#         print(f'- {hobby}')
#     print(f' Your hobby is {hobbies}')
    
# #Calling the greet function.
# greet ('Srikanth', 'watching-TV', 'driving')




#For example if we have to privide multiple variable as a key:value format in a function eg:hobby=hobbies, below is the programme.
def Info(name, **information):
    print('')
    print(f'Information of {name}')
    for key,value in information.items():
        print(f'{key} is {value}')
    print(f'Thank you for signing in {name}')
    
#Calling the function
Info ('Srikanth', age=30, height=6, email='srikanth.email.com')
Info ('Lasya')



#Return of results in a function Ex:below.
def add(num1, num2):
    return num1 + num2
result = add(10, 20)
print(result)
