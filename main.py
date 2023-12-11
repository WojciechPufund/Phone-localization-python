import phonenumbers
import opencage
import folium
from mynumber import number
from phonenumbers import geocoder
from phonenumbers import carrier
from opencage.geocoder import OpenCageGeocode


pepnumber = phonenumbers.parse(number)
location = geocoder.description_for_number(pepnumber, "pl")

print(location)

service_pro = phonenumbers.parse(number)
print(carrier.name_for_number(service_pro, "pl"))

#https://opencagedata.com/dashboard#geocoding
key = 'dd7dba7443834b9797b2492338e57362'

geocoder = OpenCageGeocode(key)
query = str(location)
results = geocoder.geocode(query)
#print(results)

lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']
print(lat, lng)


myMap = folium.Map(location=[lat, lng], zoom_start=9)
folium.Marker([lat, lng], popup=location).add_to(myMap)

myMap.save("mylocation.html")
