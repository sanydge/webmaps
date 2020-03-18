import folium

map = folium.Map(location=[46.738926, 23.477035], zoom_start=6, tiles="Stamen Terrain")
map.save("Map1.html")

