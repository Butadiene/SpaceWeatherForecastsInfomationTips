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
        "X-ray flux": create_child_object("GOES X-ray Flux", "https://www.swpc.noaa.gov/products/goes-x-ray-flux/", True, \
                    purpose="GOES background X-ray flux",file_type="graphs", exampleVal="B7, 穏やかに上昇中", \
                    memo="GOES衛星が捉えた太陽からのX線の量。太陽活動の重要な指標。赤やオレンジのGOES-16 long, GOES-18 longの値を見ると、ちゃんとC4.7みたいな値がわかる。"),

        "Solar radio flux": create_child_object("DRAO", "https://www.spaceweather.gc.ca/forecast-prevision/solar-solaire/solarflux/sx-5-en.php", True,\
                            purpose="F10.7", file_type="html", \
                            memo="太陽黒点数と良い相関のある、波長10.7cm(周波数2.8GHz)の電波の強度。Daily flux valuesのHTML見れば良いけど、\
                            めちゃ見づらいので注意。値はObserved fluxを使用すると良さそう。極大期では月平均でおおよそ200、極小期では70程度（日単位では変動が大きく、300を超えることも。）"),

        "Sun spot": { **create_child_object("SOLAR REGION SUMMARY", "https://www.swpc.noaa.gov/products/solar-region-summary", False, \
                        purpose="Sunspot area (SWPC) & Charactistics of active regions", file_type="text", exampleVal="Sunspot area : 660, 穏やかに上昇中  Charactistics of active regions : 領域、位置、面積...", \
                        memo="現在の太陽黒点の一覧とその性質が載っている。黒点の総面積を出したいときはすべて足す。その黒点がいつから発生したかを知りたいときは、過去のデータを参照すると良い。\
                            なお、過去のデータはftpでテキストファイルでしか配布されていない。Dataのところにあるリンクを使うなどすると良い。例：ftp://ftp.swpc.noaa.gov/pub/forecasts/にアクセスし、SRSフォルダの中のテキストファイルを確認"),

                    **create_child_object("SILSO : Daily estimated sunspot number", "https://www.sidc.be/SILSO/home", False, \
                      purpose= "Relative sunspot number", file_type="text", exampleVal="109, 一定", \
                      memo="太陽黒点相対数。太陽光球面に出現する黒点および黒点群の総数を数値化したもの。サイトのホームの右端にあるね。"),

                    **create_child_object("SILSO : Monthly relative sunspot number", "NoURL", False, \
                      purpose= "Monthly relative sunspot number", file_type="text", exampleVal="Result: Jul-23 159.1   Forecast: Aug-23 154, Sep-23 160", \
                      memo="太陽黒点相対数の月平均。予測値も見れる。月平均の値なので、一月に一回しか更新されない。")
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
