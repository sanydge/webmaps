import folium
import pandas as pd

df = pd.read_csv("Volcanoes.txt")

lat = list(df["LAT"])
lon = list(df["LON"])

map = folium.Map(location=[44.421054, -117.814664], zoom_start=6, tiles="Stamen Terrain")

fg = folium.FeatureGroup(name="My Map")

for lt, ln in zip(lat, lon):
    fg.add_child(folium.Marker(location=[lt, ln], popup="I am a Marker", icon=folium.Icon(color='green')))

map.add_child(fg)

map.save("Map1.html")

