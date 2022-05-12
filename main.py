import map
import folium

def main():
    map()

    # The map will center it's location to Saskatoon.
    # The coordinates provided is for Saskatoon.
    map = folium.Map(location=[52.146973,-106.647034], zoom_started=6, tiles="Stamen Terrain")

    map.add_child(fg)
    map.save("Map_SK.html")

if __name__ == "__main__":
    main()