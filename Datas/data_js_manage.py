import json

def create_child_object(name, url, external_access, memo=None, Purpose=None, file_type=None):
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
    if Purpose:
        child[name]["Purpose"] = Purpose
    return child

# Now let's use the above function to create the structure

space_weather_info = {
    "solar_flares": {
        "GOES"
        "sunspot_data": create_child_object("Sunspot Observatory", "http://example.com/sunspot", True, memo="Sunspot data source"),
        "flare_data": create_child_object("Solar Flare Monitor", "http://example.com/flare", True),
        "solar_image": create_child_object("Solar Image Gallery", "http://example.com/solarimage", True),
        # Add other objects for solar flares here using create_child_object()
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
    json.dump(space_weather_info, f, indent=4)

"/mnt/data/space_weather_info.json"
