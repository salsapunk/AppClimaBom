import requests
from geo.py import Localidade
#importar as variaveis de ambiente .env

lat = Localidade.latitude
lon = Localidade.longitude
API_KEY = "c2644944fba7092e7710bf42b3125bec"

url = f'https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={API_KEY}'

response = requests.get(url)

if response:
    print("Sucesso!")
else:
    raise Exception(f"Código de erro: {response.status_code}")

dicionario = response.json()

print(dicionario)

#dt -> unix utc data e hora
    #main:
        #temp
        #feels_like
        #temp_min
        #temp_max
        #humidity
    #wind:
        #speed

class Clima_localidade():
    def __init__(self):
        temperatura = None          #int (°C, °F)
        sens_termica = None         #int (°C, °F)
        umidade = None              #float (%)
        vento_velocidade = None     #float  (m/s)
        vento_direcao = None        #float  (deg.)

    def obter_temperatura():
        None

    def obter_sens_termica():
        None

    def obter_umidade():
        None

    def obter_vel_vento():
        None

    def obter_vento_direcao():
        None
