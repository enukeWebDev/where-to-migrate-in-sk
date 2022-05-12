import folium
import pandas

def map():
    # Access the SK_Profile file
    data = pandas.read_csv("SK_Profile.txt")
    lat = list(data["LAT"])
    lon = list(data["LON"])
    cit = list(data["CITY"])
    pop = list(data["POPULATION"])
    cri = list(data["CRIMERATE"])

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

    fg = folium.FeatureGroup(name="Saskatchewan Map")

    # Adding multiple marker on the map.
    # Iterate on the information of the Library.txt file.
    # Then assign to a new variable for easy access.
    for  lat_, lon_, cit_, pop_, cri_ in zip(lat, lon, cit, pop, cri):
        iframe = folium.IFrame(html=html % (cit_, pop_, str(cri_)+"%"), width=200, height=100)
        fg.add_child(folium.Marker(location = [lat_, lon_], \
                  popup = folium.Popup(iframe),  \
                    icon = folium.Icon(color="green")))
