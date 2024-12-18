import folium
import pandas

data = pandas.read_csv("./mapping/Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])
map = folium.Map(location=[38.58,-99.09], zoom_start=6)

mv = folium.FeatureGroup(name="Vocanoes")

def setIconColor(elevation):
    if elevation < 1000:
        return "green"
    elif 1000 <= elevation < 3000:
        return "orange"
    else:
        return "red"

for lt , ln, el in zip(lat, lon, elev):
    mv.add_child(folium.CircleMarker(location=[lt, ln], popup=str(el)+ " m",color="grey", fill_color=setIconColor(el), fill_opacity=1, radius=6))

mp = folium.FeatureGroup(name="Population")
mp.add_child(folium.GeoJson(data=open("./mapping/world.json", "r", encoding="utf-8-sig").read(),style_function= lambda x: {"fillColor":"green" if x["properties"]["POP2005"] < 10000000 else "yellow" if 10000000 <= x["properties"]["POP2005"] < 70000000 else "red"}))


map.add_child(mv)
map.add_child(mp)
map.add_child(folium.LayerControl())
map.save("./mapping/map1.html")
