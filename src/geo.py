from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="AppClima")
Localidade = geolocator.geocode("Maceió AL")
# print(Localidade.address)
# print((Localidade.latitude, Localidade.longitude))
