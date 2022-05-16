# Different color to identify crime rate for each marker on the map.

def crime_rate_identifier(cr):
        if cr > 300:
            return "red"
        elif 200 <= cr <= 299:
            return "black"
        elif 100 <= cr <= 199:
            return "purple"
        else:
            return "green"

