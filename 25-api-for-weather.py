
#This programme is to use the API calls to get the weather report of a particular city with user input as city name.

#Here we are using openweathermap.org website API. We need to sign up here to use the API's.

#Username:srikanthj2311 pass:srikanth1234.

import requests

API_KEY = '92bc798aa702affc861f61c5279b59a9'
city_name = input('Enter the name of the city: ')

url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}'   #API key that we get from the weather site.

response = requests.get(url)
print(response)                      #This gives the response codes from the API like 200,300,400,500
                                     #status code 200 - OK. status code indicates your request got success.
                                     #status code 300 - Read other. status code indicates your request is redirected to some other location.
                                     #status code 400 - Bad Request. status code indicates your request is not correct.
                                     #status code 500 - Internal Server Error. status code indicates there is no response from server end.
if response.status_code == 200:
    weather_data = response.json()   #To get the response data in json format.
    print(weather_data)
    weather_description = weather_data['weather'][0]['description']  #To get the details from json key,value data.
    print(weather_description)
    temperature = weather_data['main']['temp'] - 273.15   #This is to get the temp in Celcius instead of Kelvin. 0 degree Celcius = -273.15 Kelvin.
    print(temperature)
    
    #Display the wether information for the given city.
    print(f'Weather in {city_name} is {round(temperature, 2)} with {weather_description}')   #Here round is function used to print only 2 values after the decimal point eg:30.99 degree temparature.
    
else:
    print(f'city name {city_name} is not found or incorrect')
    