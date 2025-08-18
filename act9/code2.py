import folium
import os
import displayMap as dm
os.chdir("C:\Users\benjie\Desktop\python\data")

loc = [9.300001465113539, 123.30290810830404]
map = folium.Map(location = loc, zoom_start = 18)
dm.showMap(map)