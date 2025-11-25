import requests
from geopy.geocoders import Nominatim

# from dateutil import parser as dateparser
from clima import Clima_localidade

geolocator = Nominatim(user_agent="AppClima")
# openmeteo = openmeteo_requests.Client()


class Resposta:
    def __init__(self, cidade, estado):
        Localidade = geolocator.geocode(f"{cidade} {estado}")

        self.lat = Localidade.latitude
        self.lon = Localidade.longitude
        # self.API_KEY = "i2ovf15f9v0koyqra95q3eeff0idja79yghm6p0v"
        self.data = None
        self.d_clima = None

    def requisicao(self):
        url = "https://api.open-meteo.com/v1/forecast"
        params = {
            "latitude": self.lat,
            "longitude": self.lon,
            #            "hourly": ",".join(
            #                [
            #                    "temperature_2m",
            #                    "relative_humidity_2m",
            #                    "apparent_temperature",
            #                    "precipitation_probability",
            #                    "wind_speed_10m",
            #                ]
            #            ),
            "daily": ",".join(
                [
                    "apparent_temperature_mean",
                    "temperature_2m_mean",
                    "relative_humidity_2m_mean",
                    "wind_speed_10m_mean",
                    "precipitation_sum",
                ]
            ),
            "timezone": "auto",
        }

        try:
            resp = requests.get(url, params=params, timeout=10)
        except requests.RequestsException as e:
            raise RuntimeError(f"Erro na requisição da API Open-meteo: {e}")

        self.data = resp.json()
        self.separar_respostas()

    def separar_respostas(self):
        if not self.data:
            raise RuntimeError("Nenhum dado disponível para separar")

        # hora = self.data.get("hourly", {})
        diario = self.data.get("daily", {})

        print(diario)

        clima_dia = []

        for i in range(7):
            clima_dia.append(
                {
                    "Dia": diario["time"][i],
                    "Temperatura": diario["temperature_2m_mean"][i],
                    "Sensação térmica": diario["apparent_temperature_mean"][i],
                    "Humidade": diario["relative_humidity_2m_mean"][i],
                    "Precipitação": diario["precipitation_sum"][i],
                    "Velocidade do vento": diario["wind_speed_10m_mean"][i],
                }
            )

        self.d_clima = Clima_localidade(
            clima_dia[0],
            clima_dia[1],
            clima_dia[2],
            clima_dia[3],
            clima_dia[4],
            clima_dia[5],
            clima_dia[6],
        )


# Exemplo de utilização:
# r = Resposta("Maceió", "AL")
# r.requisicao()
# print(r.d_clima.clima_dia1)
# print()
# print(r.d_clima.clima_dia2)
# print()
# print(r.d_clima.clima_dia3)
# print()
# print(r.d_clima.clima_dia4)
# print()
# print(r.d_clima.clima_dia5)
# print()
# print(r.d_clima.clima_dia6)
# print()
# print(r.d_clima.clima_dia7)
