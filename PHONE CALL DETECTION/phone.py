import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
import folium
from opencage.geocoder import OpenCageGeocode

x = input("Enter your phone number with country code starting with '+' ")
phone_number = phonenumbers.parse(x)
print("\n Phone number's location \n")
x = geocoder.description_for_number(phone_number,"en")
print(geocoder.description_for_number(phone_number,"en"));
print(carrier.name_for_number(phone_number,"en"));
Key = "eef84b546c614385a60093db6ed2c9bf"
geocoder = OpenCageGeocode(Key)
query = str(x)
results = geocoder.geocode(query)

latitude = results[0]['geometry']['lat']
longitude = results[0]['geometry']['lng']

print(latitude,longitude)

myMap = folium.Map(loction=[latitude,longitude],zoom_start = 9)
 

folium.Marker([latitude,longitude],popup=x).add_to(myMap)
 

myMap.save("Pinpoint.html")


