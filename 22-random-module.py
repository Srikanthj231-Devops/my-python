import random                     #This is a build in module and we are importing it.

print(random.random())            #This will print the ramdom number between 0 to 1.

print(random.randint(1, 10))      #This will print the ramdom number in a given range ex:1 to 10

print(random.randrange(10, 20))   #This will print the ramdom number in a given range ex:10 to 20

print(random.uniform(3.5, 5.5))   #This will print the ramdom decimal number in a given range ex:3.5 to 5.5



fruits = ['apple', 'orange', 'banana', 'kiwi', 'berry']
print(random.choice(fruits))      #This will print the given list randomly ex:here fruits.


print(fruits)             
random.shuffle(fruits)            #This will print the list in a shuffle order.
print(fruits)



######### Dice Game ##############
while True:
    print(f'The number is {random.randint(1, 6)}')
    user_input=input('Do you want to continue y/n: ')
    if user_input == 'n':
        break
