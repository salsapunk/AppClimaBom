import requests

#pegas no menu
lat = -9
lon = -36

api_key = 123
#da pra ver quando cria um usuario no openweather api

#5 dias/ 3horas
url = f'https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={api_key}'

#request = requests.get(url)

print(url)
