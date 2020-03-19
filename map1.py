import folium
import pandas as pd

df = pd.read_csv("Volcanoes.txt")

lat = list(df["LAT"])
lon = list(df["LON"])
elev = list(df["ELEV"])


def color_producer(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'


map = folium.Map(location=[44.421054, -117.814664], zoom_start=6, tiles="Stamen Terrain")

fg = folium.FeatureGroup(name="My Map")

for lt, ln, el in zip(lat, lon, elev):
    fg.add_child(folium.Marker(location=[lt, ln], popup=folium.Popup(str(el) + "m", parse_html=True),
                               icon=folium.Icon(color=color_producer(el))))

fg2 = folium.FeatureGroup("Population")
fg2.add_child(folium.GeoJson(data=open('world.json', encoding='utf-8-sig').read(),
                             style_function=lambda x: {'fillColor': 'green' if x['properties']['POP2005'] < 10000000
                             else 'orange' if 10000000 <= x['properties']['POP2005']
                                              < 20000000 else 'red'}))

map.add_child(fg2)

map.add_child(fg)

map.save("Map1.html")
