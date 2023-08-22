import json

def create_child_object(name, url, external_access, purpose=None, exampleVal=None, file_type=None, memo=None):
    """
    Creates a child object based on the provided attributes.
    
    Args:
    - name (str): Name of the linked site.
    - url (str): URL of the linked site.
    - external_access (bool): External access status.
    - memo (str, optional): Additional memo for the linked site. Default is None.
    
    Returns:
    - dict: A dictionary representing the child object.
    """
    child = {
        name: {
            "URL": url,
            "External access": external_access
        }
    }
    if memo:
        child[name]["Memo"] = memo
    if file_type:
        child[name]["File_type"] = file_type
    if purpose:
        child[name]["Purpose"] = purpose
    if exampleVal:
        child[name]["ExampleValue"] = exampleVal
    return child

# Now let's use the above function to create the structure

space_weather_info = {
    "Solar_flares": {
        "X-ray flux": { **create_child_object("GOES X-ray Flux", "https://www.swpc.noaa.gov/products/goes-x-ray-flux/", True, \
                    purpose="GOES background X-ray flux",file_type="graphs", exampleVal="B7, 穏やかに上昇中", \
                    memo="赤やオレンジのGOES-16 long, GOES-18 longの値を見ると、ちゃんとC4.7みたいな値がわかる。"),

                  **create_child_object("GOEX-ray Flux", "https://www.swpc.noaa.gov/products/goes-x-ray-flux/", True, \
                    purpose="GOES background X-ray flux",file_type="graphs", exampleVal="148.7, 一定", \
                    memo="赤やオレンジのGOES-16 long, GOES-18 longの値を見ると、ちゃんとC4.7みたいな値がわかる。")
        },

        "Solar radio flux": create_child_object("DRAO", "https://www.spaceweather.gc.ca/forecast-prevision/solar-solaire/solarflux/sx-5-en.php", True,\
                            purpose="F10.7", file_type="html", \
                            memo="太陽黒点数と良い相関のある、波長10.7cm(周波数2.8GHz)の電波の強度。Daily flux valuesのHTML見れば良いけど、\
                            めちゃ見づらいので注意。値はObserved fluxを使用しているよう。極大期では月平均でおおよそ200、極小期では70程度（日単位では変動が大きく、300を超えることも。）"),

        "Sun spot": { **create_child_object("SWPC", "hogeURL", False, \
                        purpose="Sunspot area", file_type="", exampleVal="660, 穏やかに上昇中", \
                        memo=""),
                    **create_child_object("SILSO", "hogeURL", False, \
                      purpose= "Relative sunspot number and Monthly Relative sunspot number", file_type="", exampleVal="109, 一定", \
                      memo="")
                    },
        
    },
    "solar_wind": {
        "solar_wind_data": create_child_object("Solar Wind Monitor", "http://example.com/solarwind", True),
        "simulation": create_child_object("Solar Wind Simulation", "http://example.com/solarwindsimulation", True, memo="Simulation tool for solar wind"),
        "image": create_child_object("Solar Wind Image Gallery", "http://example.com/solarwindimage", True),
        "CME": create_child_object("CME Tracker", "http://example.com/cme", True),
        # Add other objects for solar wind here using create_child_object()
    },
    "geomagnetic_disturbances": {
        "geomagnetic_data": create_child_object("Geomagnetic Data Center", "http://example.com/geomagneticdata", True),
        "AE/Dst_index": create_child_object("AE/Dst Index Tracker", "http://example.com/aedst", True),
        "simulation": create_child_object("Geomagnetic Disturbance Simulation", "http://example.com/geomagneticsimulation", True),
        "aurora": create_child_object("Aurora Watch", "http://example.com/aurora", True, memo="Aurora observation platform"),
        # Add other objects for geomagnetic disturbances here using create_child_object()
    },
    "ionosphere": {
        # Add similar structure for ionosphere here using create_child_object()
    }
    # Add other top-level objects here using create_child_object()
}

# Save to a JSON file
with open("./Datas/space_weather_info.json", "w") as f:
    json.dump(space_weather_info, f, indent=4, ensure_ascii=False)

"/mnt/data/space_weather_info.json"
