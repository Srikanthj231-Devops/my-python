
# Sets are unordered and uniq elements.

my_set = {'mon','tue','wed','mon'}
print(type(my_set))                      # To check the type of lists. Result=<class 'set'>.
print(my_set)                            # In sets duplicates are not allowed.This will not print the duplicate values as well.

days = ('mon','tue','wed','thu','mon')   # This will print the duplicate values as well.
print(days)

my_set.add('thu')                        # This is to add a new value into the sets.
my_set.add('mon')                        # We cannot add the duplicates into the sets.


my_list = ['mon','tue','tue','wed','thu','mon','fri','fri']  # This is lists not sets.
print(my_list)
print(type(my_list))


days = set(my_list)                      # Here we are taking the input of list to sets to filter the duplicate values.
print(days)

