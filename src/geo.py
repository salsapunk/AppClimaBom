from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="AppClima")
location = geolocator.geocode("Maceió AL")
print(location.address)
print((location.latitude, location.longitude))