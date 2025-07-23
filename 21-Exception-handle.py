
#Exception Handling

print(10 + 2)
print(10 - 2)
print(10 / 2)
try:
    print(10 / 0)
except ZeroDivisionError:                        #Here we are handling the error 'ZeroDivisionError' from output by using 'try' and proceeding with remaining code of lines.
    print('Kindly do not divide by ZERO')        #This is to print a message in the output instead of a error.
print(10 * 2)





#File not found error
try:
    with open('user_info.txt', 'r') as file:     #Here i have given the wrong file name to check the 'try' Exception handle.
        content=file.readlines()
        print(content)
except FileNotFoundError:
    print('file does not present in this location')
else:
    for line in content:
        print(f'Welcome {line.rstrip()}')        #We are using rstrip to not to have a space between the lines.
        



#File not found error with Exception if we do not know the Exceptions
try:
    with open('user_info.txt', 'r') as file:     #Here i have given the wrong file name to check the 'try' Exception handle.
        content=file.readlines()
        print(content)
except Exception as e:                           #Here if we do not know the error, we can use Exception in 'try' and type to get the error type.
    print(e, type(e))                            #Give the wrong file name in line no. 33 and try this.
    print('file does not present in this location')
else:
    for line in content:
        print(f'Welcome {line.rstrip()}')        #We are using rstrip to not to have a space between the lines.
finally:
    print('DB closed')                           #We use this finally: to print the last message irrespective of Exceptions.
    
        
        
    
    
    
