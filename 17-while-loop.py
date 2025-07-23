# print('......Prgramme to check whether a given number is EVEN or ODD.........')

# print('')


# user_input = " "
# while user_input != 'q':
#     user_input = int(input('Enter a number to check whether it is EVEN or ODD or enter q for exit - '))
#     if user_input.isdigit():
#         if user_input % 2 == 0:
#             print('The number is EVEN')
#         else:
#             print('The number is ODD')
        
        
    

# # print('Enter a number to check whether it is EVEN or ODD number')


# # user_input = ""

# # while user_input != 'q':
# #     user_input = (int('Enter a num or q for quit: '))
# #     num = int(input('Enter a number to check EVEN or ODD - '))
# #     if num % 2 == 0:
# #         print('The number is EVEN')
# #     else:
# #         print('The number is ODD')         #This program should will be run everytime when we enter a number.It exists once it we give a number saying EVEN or ODD.





# print("......Programme to check whether a given number is EVEN or ODD.........")

# while True:
#     user_input = input("Enter a number to check whether it is EVEN or ODD or enter q to exit - ")

#     if user_input.lower() == 'q':
#         print("Exiting the program.")
#         break

#     if user_input.isdigit():
#         num = int(user_input)
#         if num % 2 == 0:
#             print(f"{num} is EVEN.\n")
#         else:
#             print(f"{num} is ODD.\n")
#     else:
#         print("Invalid input. Please enter a valid number or 'q' to quit.\n")




##########...To repeat the while loop until the count is ready eg:10 count......##########   
# count=1
# while count <= 10:
#     print(count)
#     count += 1


##########...Programme to print a user message until quit......##########  
# msg=''
# while msg != 'quit':
#     msg=input('Enter a message - ')
#     print(msg)


##########...Programme to print a user message until exit......########## 
# active=True
# while active:
#     msg = input('Enter a message - ')
#     if msg == 'exit':
#         active=False
        
        
##########...Programme to delete a number in a string till the number is deleted......########## 
# num = [2,4,6,8,10,4,5,4,12,4]
# while 4 in num:
#     num.remove(4)
#     print(num)
    
    

##########...Using 'break' to quit the programme in between......########## 
message=''
while True:
    message = input('Enter your message - ')
    if message == 'quit':
        break
    else:
        print(message)
            