import folium
import os
import webbrowser

# Location
loc = [9.300001465113539, 123.30290810830404]

# Create map
m = folium.Map(location=loc, zoom_start=18)

# Add marker
folium.Marker(
    location=loc,
    icon=folium.Icon(color='red', icon='star')
).add_to(m)

# Save map as HTML
map_path = os.path.abspath("map.html")
m.save(map_path)

# --- Force open with Chrome (update path if needed) ---
chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
webbrowser.get(f'"{chrome_path}" %s').open(map_path)
