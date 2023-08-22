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
                    memo="GOES衛星が捉えた太陽からのX線の量。太陽活動の重要な指標。 <br> 赤やオレンジのGOES-16 long, GOES-18 longの値を見ると、ちゃんとC4.7みたいな値がわかる。"),

        "Solar radio flux": create_child_object("DRAO", "https://www.spaceweather.gc.ca/forecast-prevision/solar-solaire/solarflux/sx-5-en.php", True,\
                            purpose="F10.7", file_type="html", \
                            memo="太陽黒点数と良い相関のある、波長10.7cm(周波数2.8GHz)の電波の強度。Daily flux valuesのHTML見れば良いけど、\
                            めちゃ見づらいので注意。値はObserved fluxを使用すると良さそう。 <br> 極大期では月平均でおおよそ200、極小期では70程度(日単位では変動が大きく、300を超えることも。)"),

        "Sun spot": { **create_child_object("SOLAR REGION SUMMARY", "https://www.swpc.noaa.gov/products/solar-region-summary", True, \
                        purpose="Sunspot area (SWPC) & Charactistics of active regions", file_type="text", exampleVal="Sunspot area : 660, 穏やかに上昇中 <br> Charactistics of active regions : 領域、位置、面積...", \
                        memo="現在の太陽黒点の一覧とその性質が載っている。黒点の総面積を出したいときはすべて足す。その黒点がいつから発生したかを知りたいときは、過去のデータを参照すると良い。\
                            <br> なお、過去のデータはftpでテキストファイルでしか配布されていない。Dataのところにあるリンクを使うなどすると良い。例：ftp://ftp.swpc.noaa.gov/pub/forecasts/にアクセスし、SRSフォルダの中のテキストファイルを確認"),

                    **create_child_object("SILSO : Daily estimated sunspot number", "https://www.sidc.be/SILSO/home", True, \
                      purpose= "Relative sunspot number", file_type="text", exampleVal="109, 一定", \
                      memo="太陽黒点相対数。太陽光球面に出現する黒点および黒点群の総数を数値化したもの。サイトのホームの右端にあるね。"),

                    **create_child_object("SILSO : Monthly relative sunspot number", "https://www.sidc.be/products/ri/", True, \
                      purpose= "Monthly relative sunspot number", file_type="text", exampleVal="Result: Jul-23 159.1   Forecast: Aug-23 154, Sep-23 160", \
                      memo="太陽黒点相対数の月平均。予測値も見れる。月平均の値なので、一月に一回しか更新されない。")
        },
        "Solar image": { **create_child_object("SDO Images", "https://sdo.gsfc.nasa.gov/data/", True, \
                        purpose="Confirmation of solar surface activity, coronal holes, CMEs and others", file_type="images", exampleVal="AIA 094's image is..., AIA 1700 image is...",\
                        memo = "SDO衛星による取得画像。波長ごとに見れるので、そこから太陽表面の概観がわかる。AIA/HMI Browse Dataのところとか覗くとわかりやすいかも。\
                            <br> 主なもの： <br> AIA 094 (green)-エネルギーがかなり高い。CMEの発生とかよく見える。 <br> AIA 211 (purple)-greenよりエネルギーが低い。コロナホールが見えやすい。 <br> AIA 171 (gold)-エネルギー的にはgreenとpurpleの間。一番メジャー。\
                             <br> AIA 1600 (yellow/green)-低めのエネルギー。彩層底部（光球上部）の光が見える。フレアの発生を示唆する。遷移層の光も混じるので注意。 <br> HMI Intensitygram-光球が見える。黒点がわかりやすい。 \
                             <br> HMI Magnetogram-可視光による偏光観測。黒点の磁場構造が見える。この構造が複雑かつ大規模であるほど、大規模フレアが起きる傾向 <br> より詳しくは https://aia.lmsal.com/public/instrument.htm"),
                        
                        **create_child_object("SOHO Sunspots", "https://soho.nascom.nasa.gov/sunspots/", True, \
                        purpose= "Check sunspot numbers with sunspot images", file_type="images", 
                        memo= "SOHOの白黒光球画像。黒点が番号付きで表示されるので良い。"),

                        **create_child_object("STEREO-360 images", "https://stereo-ssc.nascom.nasa.gov/beacon/beacon_secchi.shtml", True, \
                                              "360-images for Sun", file_type= "images",\
                                                memo="STEREO衛星による太陽の360度画像。(実際は結構欠損してるけど)。地球から見えないところが気になる時に。ページの少し下のSDOの画像の中に混じっているSTEREO Aheadも参考に使えるかも。")
        },

        "Flare forecast by Deep Learning": create_child_object("Deep Flare Net", "https://defn.nict.go.jp/index131_eng.html", True, \
                                            purpose= "Forecast solar flare", file_type="text", \
                                                memo="深層学習を使って太陽フレアの発生率を予報しているサイト。参考に。")
        
    },
    "Proton flux": {
        "Proton flux": create_child_object("GOES Proton Flux", "https://www.swpc.noaa.gov/products/goes-proton-flux", True, \
                                           purpose= "Present condition of solar energetic particles", file_type='graphs',exampleVal="10^0 前後、NOAAスケールS0",\
                                            memo="Proton Fluxの変動を示す。Proton Fluxの変動は、Flux値をそのまま使って予報が出る事が多く、現況報告の意味合いが強い。\
                                                 <br> NOAAスケールとは、様々なイベントに対するNOAAが策定した指標。Proton fluxに関しては、桁数と一致(例えば、10^2を超えたらScale level S2)。詳しくは https://www.swpc.noaa.gov/noaa-scales-explanation "),

    },
    "solar_wind": {
        "CME in space": create_child_object("SOHO LASCO C2 & C3", "https://soho.nascom.nasa.gov/data/Theater/", True, \
                                            purpose="Confirmation of CME flying", file_type="images",\
                                                memo="SOHOのコロナグラフを用いた観測機器LASCOによる動画。これにより、CMEがどのように宇宙空間に広がっていったかがわかる。 <br> SDOでは、太陽表面の事象しか見れないので重要。 <br> サイトにアクセスした後、C2かC3を選び日程を設定してGenerate。C2とC3の違いは視野のみ。"),
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
