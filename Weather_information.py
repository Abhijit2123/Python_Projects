import requests
from pprint import pprint

city = input("Please enter city name: ")

API = 'cb771e45ac79a4e8e2205c0ce66ff633'

url = 'http://api.openweathermap.org/data/2.5/weather?appid='+API+'&q='+city

weather_data = requests.get(url).json()

pprint(weather_data)              #pprint - The response will be in json and not readable. This pprint will convert the json format into tree redable format.
