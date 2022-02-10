import phonenumbers
import folium
import opencage

from body import number
from phonenumbers import geocoder

key = "e1c4da593dac48c89cd77adcd578"

ch_number = phonenumbers.parse(number, "CH")
yourLocation = geocoder.description_for_number(ch_number, "en")
print(yourLocation)
from phonenumbers import carrier
service_provider = phonenumbers.parse(number, "RO")
print(carrier.name_for_number(service_provider, "en"))

from opencage.geocoder import OpenCageGeocode
geocoder = OpenCageGeocode(key)
query = str(yourLocation)
results = geocoder.geocode(query)
#print(results)
lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']

print(lat,lng)

myMap = folium.Map(location=[lat, lng], zoom_start = 9)
folium.Marker([lat, lng],popup = yourLocation).add_to(myMap)

myMap.save("myLocation.html")