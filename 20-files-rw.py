#This programme is to read and write the file in the same location or other locations with path.

with open('user_info.txt', 'w') as file:
    file.write('This is the first line we arer writimng using the python\n')    #Here \n is used to create the new content in next line.
    
    
    
with open('user_info.txt','a') as file:               #Here we are using 'a' to append the new content into the file.
    file.write('This is the second line\n')
    file.write('Srikanth\n') 
    file.write('Nainika\n')
    file.write('Lasya\n')   
    
    
with open('user_info.txt', 'r') as file:              #Here we are using 'r' to read the content in the file.
    content = file.read()
    print(content)
    

#Here we are reading the file contents line by line with Welcom in addition.
with open('user_info.txt', 'r') as file:                
    content=file.readlines()                            #This will print all the contents in a file as a list in a single line.
    print(content)
for line in content:
    print(f'Welcom {line.rstrip()}')                    #We are using rstrip to not to have a space between the lines.