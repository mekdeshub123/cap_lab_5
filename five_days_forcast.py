#the data request is limited to USA cities only
import os
import requests
from datetime import datetime
#retrieve key that stored in envromental variable  
key = os.environ.get('WEATHER_KEY')
#print(key)
print('----------------------------------------------')
print('\nTHE DATA REQUEST IS LIMITED TO US CITIES ONLY')
print('----------------------------------------------\n')
city_name = input('Enter city: ')#user imputs for the name parameter
city = city_name + ', us'# concatnates the user imput with value, us.
query = {'q': city, 'units': 'imperial', 'appid':key}#parameter in query

url = 'http://api.openweathermap.org/data/2.5/forecast'

try:
    data = requests.get(url, params=query).json()# Fetch data using get method and put it into json file
    print(data)
    
    forecast_items = data['list']#storing data into list
    print('\n')
    for forecast in forecast_items:#loop through the list
        timestamp = forecast['dt']
        date =datetime.fromtimestamp(timestamp)#convert to a readable date and time format
        temp = forecast['main']['temp']
        print(f'at {date}temprature is {temp}')# put it to format string
except:
    print('city cannot be found!')


