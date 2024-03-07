import json
from simplekml import Kml

def convert_json_to_kml(json_filename, kml_filename):
    with open(json_filename) as f:
        json_data = json.load(f)

    kml = Kml()
    for item in json_data:
        lat = item.get('lat')
        lon = item.get('lon')
        comment = f"ID: {item.get('id')}\nLocation: {item.get('loc')}\nMax Users: {item.get('maxusers')}\nAntenna: {item.get('antenna')}\nDevice: {item.get('device')}"
        kml.newpoint(name=comment, coords=[(lon, lat)])

    kml.save(kml_filename)

if __name__ == "__main__":
    convert_json_to_kml('kiwisdr.json', 'kiwisdr.kml')
    convert_json_to_kml('openwebrx.json', 'openwebrx.kml')
    convert_json_to_kml('websdr.json', 'websdr.kml')
