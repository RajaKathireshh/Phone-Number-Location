flag=True
While flag:
  ph_no=input("Enter PH NO eith +91 : ")
  if len(ph_no)==13:
    flag=False

    
pip install phonenumbers
pip install opencage
pip install folium

import phonenumbers
from phonenumbers import geocoder

no=phonenumbers.parse(ph_no)
location=geocoder.description_for_number(no,"en")
print(location)  # To find the location of the phone number

from phonenumbers import carrier
service=phonenumbers.parse(ph_no)
print(carrier.name_for_number(service,"en"))   # To find the operator


from opencage.geocoder import OpenCageGeocode

key = '2fa807adce1644eab0c115bd751a0fad'

geocoder = OpenCageGeocode(key)
query=str(location)
results=geocoder.geocode(query)
lat=results[0]['geometry']['lat']
lng=results[0]['geometry']['lng']
print(lat,lng)                      # To find the lat and lng coordinates

import folium

mymap=folium.Map(location=[lat,lng],zoom_start=9)
folium.Marker([lat,lng],popup=location).add_to(mymap)
mymap.save("location.html")   # To find the location in the map

