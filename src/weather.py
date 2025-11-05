import requests

#pegas no menu
lat = None
lon = None

#definidas aqui
time = None
API_key = None #da pra ver quando cria um usuario no openweather api

url = 'https://api.openweathermap.org/data/3.0/onecall/timemachine?lat={lat}&lon={lon}&dt={time}&appid={API_key}'

request = requests.get(url)