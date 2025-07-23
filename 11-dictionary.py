
#Dictionary is agin the list but it store the values in the key:value format.

# Eg: Marks = (30,40,50) This is list of marks.

# Dictionary Eg: Marks = ('Hindi':30, 'English':40, 'Maths':50) This is key:value format.

Marks = {'Hindi':20, 'English':30, 'Maths':90}

print(type(Marks))           # This will print the type of list Eg:<class 'dict'>.

print(Marks)                 # To print all the Marks in key:value format.
print(Marks['Hindi'])        # To print the values of particular key from the list.
print(Marks.get('English'))  # This will print the vlaue of English by using get.

print(Marks.get('Maths'))    # This will return as "None" instead of throwing an error because this Key is not present in the list.

Marks['Maths'] = 90          # We can add more key and values uing this way. Output: {'Hindi': 20, 'English': 30, 'Maths': 90}
print(Marks)

print(Marks.get('Maths'))    # This will show the value of Maths now.

del Marks['Hindi']           # To delete a particular key and value from the list.
print(Marks)

print(len(Marks))            # To print the number of key:values in the list.  