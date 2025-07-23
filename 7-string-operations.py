#Variables
f_name='Jindam'
l_name='Srikanth'

full_name=f_name +' '+ l_name    #We can also give the space in between by using '_'

print(full_name)

print(full_name.upper())  #To get the print message in Upper case.
print(full_name.lower())  #To get the print message in Lower case.
print(full_name.split())  #To get the print message in split way like ['Jindam','srikanth']
print(full_name.title())  #To get the print message in Title way like Jindam Srikanth.

message='Hello srikanth! how are you'
print(message.upper())
print(message.split('!'))
print(message[0])         #To get the print message only for the first letter in the message variable.This stores values in index format starting with index[0]
print(message[0:5])       #To get the print message only for the first word in the message variable.
print(message[-1])        #To get the print message only for the last letter in the message variable.This is indexing from the last in a line.