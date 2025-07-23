#In this script we are calling calculation.py as a module to use their programme.

import calculation

result = calculation.add(10,40)
print(result)

calculation.even_or_odd(45)

result = calculation.sub(100, 40)
print(result)

result = calculation.mul(100, 100)
print(result)


#Here we are calling the calculation file in which functions are defined as a module.