import folium
import pandas
from crimerate_color import crime_rate_identifier
from markers_info import markers_i

def map():
    
    # Access the SK_Profile file
    data = pandas.read_csv("SK_Profile.txt")
    lat = list(data["LAT"])
    lon = list(data["LON"])
    cit = list(data["CITY"])
    pop = list(data["POPULATION"])
    crime = list(data["CRIMERATE"])
    unemp = list(data["UNEMPLOYMENT"])

    # The map will center it's location to Saskatoon.
    # The coordinates provided is for Saskatoon.
    map = folium.Map(location=[52.146973,-106.647034], zoom_started=6, tiles="Stamen Terrain")
    fg = folium.FeatureGroup(name="Saskatchewan Map")

    # Adding multiple marker on the map.
    # Iterate on the information of the SK_Profile.txt file.
    # Then assign to a new variable for easy access.
    for  lat_, lon_, cit_, pop_, crime_, unemp_ in zip(lat, lon, cit, pop, crime, unemp):
        iframe = folium.IFrame(html=markers_i() % (cit_, pop_, str(crime_)+"%", str(unemp_)+"%"), \
                    width=200, height=100)

        fg.add_child(folium.Marker(location = [lat_, lon_], \
                  popup = folium.Popup(iframe),  \
                    icon = folium.Icon(color=crime_rate_identifier(crime_))))
  
    map.add_child(fg)
    map.save("Map_SK.html")

