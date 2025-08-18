import folium
import os
from geopy.geocoders import Nominatim
import displayMap as dm
import time 

geocolor = Nominatim(user_agent= "my_map_app")
address = "6201 Negros Oriental, Sibulan" 
location = geocolor.geocode(address)
loc = [location.latitude, location.longitude]
map = folium.Map(location = loc, zoom_start = 18)
dm.showMap(map)