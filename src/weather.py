import requests
#importar as variaveis de ambiente .env

url = f'https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={API_KEY}'

request = requests.get(url)

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
