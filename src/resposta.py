import requests
from geopy.geocoders import Nominatim
from clima import Clima_localidade

geolocator = Nominatim(user_agent="AppClima")


class Resposta:
    def __init__(self, cidade, estado):
        Localidade = geolocator.geocode(f"{cidade} {estado}")

        self.lat = Localidade.latitude
        self.lon = Localidade.longitude
        self.API_KEY = "i2ovf15f9v0koyqra95q3eeff0idja79yghm6p0v"
        self.data = None
        self.d_clima = None

    def request_data(self):
        url = "https://api.open-meteo.com/v1/forecast"
        params = {
            "latitude": self.lat,
            "longitude": self.lon,
            "hourly": ",".join(
                [
                    "temperature_2m",
                    "relative_humidity_2m",
                    "apparent_temperature",
                    "precipitation_probability",
                    "wind_speed_10m",
                ]
            ),
            "daily": ",".join(
                [
                    "apparent_temperature_mean",
                    "temperature_2m_mean",
                    "temperature_2m_min",
                    "temperature_2m_max", 
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

    def request_alerts(self):
        url = f"https://www.meteosource.com/api/v1/free/point?lat={self.lat}&lon={self.lon}&sections=alerts&timezone=UTC&language=en&units=metric&key={self.API_KEY}"

        try:
            resp = requests.get(url)
        except requests.RequestsException as e:
            raise RuntimeError(f"Erro na requisição da API Meteosource: {e}")
        self.alerts = resp.json()

    def requisicao(self):
        self.request_data()
        self.request_alerts()
        self.separar_respostas()

    def separar_respostas(self):
        if not self.data:
            raise RuntimeError("Nenhum dado disponível para separar")
        if not self.alerts:
            raise RuntimeError("Nenhum alerta disponível para separar")

        # separando os alertas
        alerta = []
        if self.alerts["current"] is None:
            alerta = None
        else:
            alerta.append(
                {
                    "evento": self.alerts["current"]["alerts.event"],
                    "comeco": self.alerts["current"]["alerts.onset"],
                    "fim": self.alerts["current"]["alerts.expires"],
                    "emissor": self.alerts["current"]["alerts.sender"],
                    "severidade": self.alerts["current"]["alerts.severity"],
                    "descricao": self.alerts["current"]["alerts.description"],
                }
            )

        # separando as informações
        diario = self.data.get("daily", {})

        clima_semana = []

        for i in range(7):
            clima_semana.append(
                {
                    "dia": diario["time"][i],
                    "temperatura": diario["temperature_2m_mean"][i],
                    "temperatura_min": diario["temperature_2m_min"][i],
                    "temperatura_max": diario["temperature_2m_max"][i], 
                    "sensacao_termica": diario["apparent_temperature_mean"][i],
                    "humidade": diario["relative_humidity_2m_mean"][i],
                    "precipitacao": diario["precipitation_sum"][i],
                    "velocidade_do_vento": diario["wind_speed_10m_mean"][i]
                }
            )

        horario = self.data.get("hourly", {})

        dia = []

        for i in range(7):
            hora = []
            for i in range(24):
                hora.append(
                    {
                        "hora": horario["time"][i],
                        "temperatura": horario["temperature_2m"][i],
                        "humidade": horario["relative_humidity_2m"][i],
                        "sensacao_termica": horario["apparent_temperature"][i],
                        "chance_de_precipitacao": horario["precipitation_probability"][
                            i
                        ],
                        "velocidade_do_vento": horario["wind_speed_10m"][i],
                    }
                )
            dia.append(hora)

        self.d_clima = Clima_localidade(clima_semana, dia, alerta)


# Exemplo de utilização:
r = Resposta("Maceió", "AL")
r.requisicao()
# print(r.d_clima.clima_semana)
# print()
# print(r.d_clima.clima_horas)
# print()
print(r.d_clima.alertas)

# print(r.d_clima.clima_horas[0][3])
