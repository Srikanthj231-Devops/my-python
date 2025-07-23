import datetime

from datetime import timedelta

#from datetime import datetime        #Another way of importing module.

# print(datetime.datetime.now())

# cur_date = datetime.datetime.now()
# print(cur_date.date())
# print(cur_date.time())


#Date and Time formatting in our required format eg: YY/MM/DD

print(datetime.datetime.now())
current_date_time = datetime.datetime.now()
print(current_date_time.date())                               #This will print only the date.We can also use time,day,year,month.
formatted_date = current_date_time.strftime('%Y/%m/%d')       #This is the required formatted date. Here 'm' and 'd' should be small.
print(formatted_date)

future_date = datetime.datetime.now() + timedelta(days=20)    #This will print the date 20 days a head of current date.For this we need to use "from datetime import timedelta" module.
print(future_date)                                            #We can print the future date and past date by using arithmetic operations '+' or '-'