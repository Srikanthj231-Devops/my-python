
# Example of 'for-loop' using the direct values.
for i in 1,2,3,4,5:
    print(i)
    


    
# Example of 'for-loop' using the values in a list format.
user_list = ('Srikanth','Lasya','Nainika',20,30)
for users in user_list:
    print(users)
    
    
    
    
# Example of 'for-loop' using the dictionary in key,value format.
marks = {
    'Telugu':80,
    'Social':70
}
marks = {'Hindi':80, 'English':90, 'Maths':99}
for subject, marks in marks.items():
    print(f'The subject is {subject}')
    print(f'The marks are {marks}')
# for subject in marks.keys():                    # This is only to print the keys from the dictionary.
#     print(f'The subject is {subject}')
    
    
    
    
# Example for using the range function
for num in range(1, 11):
    print(num)