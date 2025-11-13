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
        self.resposta = None
        self.d_clima = None

    def requisicao(self):
        url = f"https://www.meteosource.com/api/v1/free/point?lat={self.lat}&lon={self.lon}&sections=current,daily,daily-parts,hourly,alerts&timezone=UTC&language=en&units=metric&key={self.API_KEY}"
        response = requests.get(url)
        if response:
            print("Sucesso!")
        else:
            raise Exception(f"Código de erro: {response.status_code}")
        self.resposta = response.json()
        self.separar_respostas()

    def separar_respostas(self):
        c = self.resposta["current"]
        dia_atual = {
            "icone": c["icon"],
            "resumo": c["summary"],
            "temperatura": c["temperature"],
            "velocidade do vento": c["wind"]["speed"],
            "direção do vento": c["wind"]["dir"],
        }
        clima_dia = []
        for i in range(7):
            hdd = self.resposta["daily"]["data"][i]
            dia = {
                "data e hora": hdd["day"],
                "clima": hdd["weather"],
                "icone": hdd["icon"],
                "temperatura": hdd["all_day"]["temperature"],
                "temperatura mínima": hdd["all_day"]["temperature_min"],
                "temperatura máxima": hdd["all_day"]["temperature_max"],
                "velocidade do vento": hdd["all_day"]["wind"]["speed"],
                "direção do vento": hdd["all_day"]["wind"]["dir"],
            }
            clima_dia.append(dia)
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
r.Resposta()
r.requisicao()
print(r.resposta)
print()
print(r.d_clima.clima_atual)
print()
print(r.d_clima.clima_dia1)
print()
print(r.d_clima.clima_dia2)
print()
print(r.d_clima.clima_dia3)
print()
print(r.d_clima.clima_dia4)
print()
print(r.d_clima.clima_dia5)
print()
print(r.d_clima.clima_dia6)
print()
print(r.d_clima.clima_dia7)
