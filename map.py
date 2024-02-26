import folium
import pandas as pd

df = pd.read_csv("Volcanoes.txt")
lat = list(df["LAT"])
lon = list(df["LON"])
elev = list(df["ELEV"])

def color_producer(elev):
    if elev < 1000:
        return 'green'
    elif 1000<= elev > 3000:
        return 'orange'
    else:
        return 'red'

map = folium.Map(location=[40.85, -101.44], zoom_start=4, tiles="Cartodb dark_matter")

fgv = folium.FeatureGroup(name="Volcanoes")

for lt, ln, elv in zip(lat, lon, elev):
    fgv.add_child(folium.CircleMarker(location=[lt,ln], radius=6, popup=str(elv)+"m",
fill_color=color_producer(elv),color="gray", fill_opacity=0.7))

fgp = folium.FeatureGroup(name="Population")

fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000 else 'orange' if 10000000 <=
x['properties']['POP2005'] < 20000000 else 'red'}))

map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())

map.save("map.html")
