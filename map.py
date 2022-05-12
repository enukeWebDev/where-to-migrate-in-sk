import folium
import pandas

# Access the Library file
data = pandas.read_csv("SK_Profile.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
cit = list(data["CITY"])
pop = list(data["POPULATION"])
cri = list(data["CRIMERATE"])
# lib = list(data["LIBRARY"])
# add = list(data["ADDRESS"])

# Adding styles using HTML.
# Can also add link.
html = """<h4>Vital Information</h4>
City: %s
<br>
Population: %s
<br>
Crime Rate: %s
<br>
"""

# The map will center it's location to Saskatoon.
# The coordinates provided is for Saskatoon.
map = folium.Map(location=[52.146973,-106.647034], zoom_started=6, tiles="Stamen Terrain")

# Adding multiple marker on the map.
fg = folium.FeatureGroup(name="Saskatchewan Map")

# Iterate on the information of the Library.txt file.
# Then assign to a new variable for easy access.
for  lat_, lon_, cit_, pop_, cri_ in zip(lat, lon, cit, pop, cri):

    iframe = folium.IFrame(html=html % (cit_, pop_, str(cri_)+"%"), width=200, height=100)

    fg.add_child(folium.Marker(location = [lat_, lon_], \
              popup = folium.Popup(iframe),  \
              # popup = folium.Popup(iframe), \
                icon = folium.Icon(color="green")))

#     fg.add_child(folium.CircleMarker(location = [lat_, lon_], radius = 10,\
#               # popup=[lib_, add_,],  \
#               popup = folium.Popup(iframe), \
#                 fill_color = (add_), color="red", fill_opacity = 1))

map.add_child(fg)
map.save("Map_SK.html")