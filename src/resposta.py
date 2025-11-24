import openmeteo_requests
from geopy.geocoders import Nominatim
from clima import Clima_localidade

geolocator = Nominatim(user_agent="AppClima")
openmeteo = openmeteo_requests.Client()

class Resposta:
    def __init__(self, cidade, estado):
        Localidade = geolocator.geocode(f"{cidade} {estado}")

        self.lat = Localidade.latitude
        self.lon = Localidade.longitude
        self.API_KEY = "i2ovf15f9v0koyqra95q3eeff0idja79yghm6p0v"
        self.resposta_c = None
        self.resposta_h = None
        self.resposta_d = None
        self.d_clima = None

    def requisicao(self):
        url = "https://api.open-meteo.com/v1/forecast"
        params = {
            "latitude":  self.lat,
            "longitude": self.lon,
            "daily": ["temperature_2m_max", "temperature_2m_min", "apparent_temperature_max", "apparent_temperature_min", "precipitation_sum", "relative_humidity_2m_mean"],
	        "hourly": ["temperature_2m", "relative_humidity_2m", "apparent_temperature", "rain", "wind_speed_10m", "precipitation_probability"],
	        "current": ["temperature_2m", "relative_humidity_2m", "apparent_temperature", "wind_speed_10m", "precipitation"],
        }
        responses = openmeteo.weather_api(url, params = params)
        if responses:
            print("Sucesso!")
        else:
            raise Exception(f"Código de erro: {response.status_code}")
        response = responses[0]
        self.resposta_c = response.Current()
        self.resposta_h = response.Hourly()
        self.resposta_d = response.Daily()
        self.separar_respostas()

    def separar_respostas(self):
        #funções p separar em dicionarios
        self.d_clima = Clima_localidade(
            dia_atual,
            clima_dia[0],
            clima_dia[1],
            clima_dia[2],
            clima_dia[3],
            clima_dia[4],
            clima_dia[5],
            clima_dia[6],
        )


# Exemplo de utilização:
r = Resposta("Maceió", "AL")
r.requisicao()
#print(r.resposta)
#print()
#print(r.d_clima.clima_atual)
#print()
#print(r.d_clima.clima_dia1)
#print()
#print(r.d_clima.clima_dia2)
#print()
#print(r.d_clima.clima_dia3)
#print()
#print(r.d_clima.clima_dia4)
#print()
#print(r.d_clima.clima_dia5)
#print()
#print(r.d_clima.clima_dia6)
#print()
#print(r.d_clima.clima_dia7)
