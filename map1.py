import folium

map = folium.Map(location=[46.738926, 23.477035], zoom_start=7, tiles="Stamen Terrain")

fg = folium.FeatureGroup(name="My Map")
fg.add_child(folium.Marker(location=[45.664260, 25.560096], popup="I am a Marker", icon=folium.Icon(color='green')))
map.add_child(fg)

map.save("Map1.html")

