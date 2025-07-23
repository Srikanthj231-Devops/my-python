
#Tuples is a type of list which is Immutable, which cannot change the values.
#Tuples store the values in serail order.
#Tuples can be stored using "()" where as a list can be stored in "[]".

days = ('Mon','Tue','Wed','Thur')

#days = (20,30)             # The Tuple values cannot be changed but we can define the new values that means we can re-assign new values to Tuple.

print(days)                 # This will print all the values in the Tuple list.

print(type(days))           # This will show the type of list.The answer is <class 'tuple'>

print(days[0])              # This will print the particular index value in the tuple-list.

print(days.count('Wed'))    # This will print the number of count the value is present.

print(days.index('Thur'))   # This will print the index number of the given value.

print(days[1])