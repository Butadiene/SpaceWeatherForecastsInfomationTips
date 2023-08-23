import json

def create_child_object(name, url, external_access, purpose=None, exampleVal=None, file_type=None, memo=None, refURL = None, refURL2 = None):
    """
    Creates a child object based on the provided attributes.
    
    Args:
    - name (str): Name of the linked site.
    - url (str): URL of the linked site.
    - external_access (bool): External access status.
    - memo (str, optional): Additional memo for the linked site. Default is None.
    - file_type (str, optional): text OR images OR graphs OR html. File type for the linked site's data. Default is None.
    - purpose (str, optional): How to use the linked site data. Default is None.
    - exampleVal (str, optional): How can the data be expressed in a way that makes it easier to communicate to others? Default is None.
    - refURL (str, optional): Reference URL for the linked site.
    - refURL2 (str, optional): Reference URL for the linked site.
    
    Returns:
    - dict: A dictionary representing the child object.
    """
    child = {
        name: {
            "URL": url,
            "External_access": external_access
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
    if refURL:
        child[name]["Reference_URL"] = refURL
    if refURL2:
        child[name]["Reference_URL2"] = refURL2
    return child

# Now let's use the above function to create the structure

space_weather_info = {

    "Space weather forecast for each country": {
        "Space weather forecast for each country": create_child_object("Present Space Weather Forecast from ISES", "https://swc.nict.go.jp/data/ises/isesforecast.html", True,\
                                                                purpose="Check space weather forecast for each country",file_type="text",\
                                                                memo="ISES(The International Space Environment Service)のメンバー国が出している宇宙天気予報を一覧で見られる。")
    },

    "Solar and geophysical events": {
        "All event reports (SWPC)": create_child_object("SWPC SOLAR AND GEOPHYSICAL EVENT REPORTS","https://www.swpc.noaa.gov/products/solar-and-geophysical-event-reports",True,\
                                purpose="Check events list",file_type="text",\
                                    memo="太陽表面や磁気圏でのイベントのリスト。日付ごとのリストになっている。主要なイベントのリスㇳになっていて重要。\
                                         <br> SWPC(Space Weather Prediction Center)から出されたリスト。\
                                         <br> BeginとENDがイベント発生と終了時間。X線観測の結果のイベント、光学観測結果のイベント等々をすべて別物として扱う。どの観測手法で、どのように検知されたかをTypeが示す。\
                                         <br> なお、異なる機器で観測されたイベントが、同じ事象によって生じたものと判断した場合、同じイベント番号を振る。\
                                         <br> サイトの少し下のDetailsのところにあるリンクからType一覧を確認できる。例：ftp://ftp.swpc.noaa.gov/pub/indices/ にアクセスし、eventsフォルダの中のREADMEを確認。\
                                         <br> また、過去のデータはftpでテキストファイルでしか配布されていない。サイトの少し下のDataのところにあるリンクから、過去のデータをダウンロードできる。\
                                         <br> 例：ftp://ftp.swpc.noaa.gov/pub/indices/ にアクセスし、eventsフォルダの中のテキストファイルを確認。"),

        "Last flare event reports (LMSAL)": create_child_object("LMSAL last event reports","https://www.lmsal.com/solarsoft/last_events/",True,\
                                purpose="Check events list",file_type="text",\
                                    memo="フレアのイベントのリスト。直近20イベントのリストになっている。 <br> 直近20イベントだけだが、NOAAのものと違ってリストで示されていたり、図もついていたりと見やすい。"),
    },

    "Solar flares": {
        "X-ray flux": create_child_object("GOES X-ray Flux", "https://www.swpc.noaa.gov/products/goes-x-ray-flux/", True, \
                    purpose="GOES background X-ray flux",file_type="graphs", exampleVal="B7, 穏やかに上昇中", \
                    memo="GOES衛星が捉えた太陽からのX線の量。太陽活動の重要な指標。 <br> 赤やオレンジのGOES-16 long, GOES-18 longの値を見ると、ちゃんとC4.7みたいな値がわかる。\
                        <br> フレアが起きていない（≒尖っていないところ）をバックグラウンドと呼んだりする。これも重要で、バックグラウンドが上昇傾向にある場合は、例えば東側から活動的な領域が見え始めていたりすることを意味する可能性がある。"),

        "Radio flux": {**create_child_object("DRAO", "https://www.spaceweather.gc.ca/forecast-prevision/solar-solaire/solarflux/sx-5-en.php", True,\
                            purpose="F10.7: 10.7cm wavelength radio wave strength", file_type="html", \
                            memo="太陽黒点数と良い相関のある、波長10.7cm(周波数2.8GHz)の電波の強度。 <br> Daily flux valuesのHTML見れば良いけど、\
                            めちゃ見づらいので注意。値はObserved fluxを使用すると良さそう。 <br> 極大期では月平均でおおよそ200、極小期では70程度(日単位では変動が大きく、300を超えることも。)"),

                        **create_child_object("山川 太陽電波望遠鏡","https://origin-swc.nict.go.jp/forecast/magnetosphere.html", True, \
                            purpose= "Solar radio burst", file_type="graphs", \
                            memo="山川での太陽電波観測結果。リンク先サイトの右やや下の方にある「太陽電波観測」から見れる。太陽電波バーストを見るのに良い。\
                                 <br> 太陽電波バーストは太陽活動を示すイベントとして重要だが、山川の観測データからイベントを識別するのは難しく、初心者向けではない。")

        },

        "Sun spot": {**create_child_object("SILSO : Daily estimated sunspot number", "https://www.sidc.be/SILSO/home", True, \
                      purpose= "Relative sunspot number", file_type="text", exampleVal="109, 一定", \
                      memo="太陽黒点相対数。太陽光球面に出現する黒点および黒点群の総数を数値化したもの。サイトのホームの右端にある。"),

                    **create_child_object("SILSO : Monthly relative sunspot number", "https://www.sidc.be/products/ri/", True, \
                      purpose= "Monthly relative sunspot number", file_type="text", exampleVal="Result: Jul-23 159.1   Forecast: Aug-23 154, Sep-23 160", \
                      memo="太陽黒点相対数の月平均。予測値も見れる。月平均の値なので、一月に一回しか更新されない。"),
            
            
                    **create_child_object("SOLAR REGION SUMMARY", "https://www.swpc.noaa.gov/products/solar-region-summary", True, \
                        purpose="Sunspot area (SWPC) & Charactistics of active regions", file_type="text", exampleVal="Sunspot area:660, 穏やかに上昇中 & Charactistics of active regions:領域、位置、面積...", \
                        memo="現在の太陽黒点の一覧とその性質が載っている。SRSと略され、重要なデータの一つ。 <br> 現在の黒点の総面積を出したいときは、SRSに載っている黒点の面積をすべて足す。その黒点がいつから発生したかを知りたいときは、過去のデータを参照すると良い。\
                            <br> Z- Modified Zurich classification of the group. 修正チューリッヒクラス。3つのアルファベットの組み合わせで表される。Reference_URL参照\
                            <br> Lo- Carrington longitude of the group.\
                            <br> LL- Longitudinal extent of the group in heliographic degrees.\
                            <br> NN- Total number of visible sunspots in the group.\
                            <br> Mag Type- Magnetic classification of the group. マウント・ウィルソン分類による黒点の分類。α、β、βγ、γ、δなどがあり、δに行くほどフレアを起こしやすいとされる。\
                            <br> &nbsp;&nbsp;δ型にだけ要警戒しておけばとりあえずは良い。\
                            <br> &nbsp;&nbsp;以下に簡単に説明。詳しくはReference_URL2参照。\
                            <br> &nbsp&nbsp;&nbsp;&nbsp;α：単極で存在するもの。\
                            <br> &nbsp&nbsp;&nbsp;&nbsp;β：2つの極から成る単純な黒点の対。つまり、2つの黒点が近くにあり、その2つの極性が逆(NとSになっている)。\
                            <br> &nbsp&nbsp;&nbsp;&nbsp;γ：β には分類しがたいような複雑な極構造を持った黒点。\
                            <br> &nbsp&nbsp;&nbsp;&nbsp;δ：2つの黒点が近くにあり、その2つの極性が逆。かつ2つの黒点は半暗部を共有している。すなわち、半暗部の中に2つの暗部があり、その2つの極性が逆になっている。一番コロナが起きやすい。\
                            <br> なお、過去のデータはftpでテキストファイルでしか配布されていない。サイトの少し下のDataのところにあるリンクから、過去のデータをダウンロードできる。 <br> 例：ftp://ftp.swpc.noaa.gov/pub/forecasts/ にアクセスし、SRSフォルダの中のテキストファイルを確認",\
                                refURL="https://www.spaceweatherlive.com/en/help/the-classification-of-sunspots-after-malde.html",\
                                refURL2="https://solarphys.com/dynamics/ar/"),
                        
                    **create_child_object("SOHO Sunspots", "https://soho.nascom.nasa.gov/sunspots/", True, \
                        purpose= "Check sunspot numbers with sunspot images", file_type="images", 
                        memo= "SOHOの白黒光球画像。黒点が番号付きで表示される。"),

                     **create_child_object("SHARP Vector Magnetograms", "https://defn.nict.go.jp/sharp/index_sharp_jp.html",True,\
                        purpose="Check degree of magnetic field distortion (shear)", file_type="images",\
                        memo="各黒点の磁場の歪み具合を画像でわかりやすく示してくれる。 <br> この構造が複雑であれば（具体的には極性が複雑でかつコンパクトにまとまった黒点）、より大きいフレアを警戒する必要がある。 \
                            <br> 特に確認すべきはシア。緑色の線(磁気中性線)と平行かつ緑色の線を挟んで逆方向に磁場が向いている場合（シアという）、よりフレアを警戒する必要がある。 <br> (緑色の断層線に沿って赤方向にずれる横ずれ断層をイメージすると良いかも。)\
                            なお、英語版はReference_URLに記載。", refURL="https://defn.nict.go.jp/sharp/index_sharp.html"),

                     **create_child_object("SHARP Data Viewer", "http://jsoc.stanford.edu/data/hmi/sharp/dataviewer/",True,\
                        purpose="Check degree of magnetic field distortion (shear)", file_type="images",\
                        memo="シアやフラックスの値などを定量的に示したのが SHARP Data Viewer。以下の2つをよく使う。\
                             <br> mean shear angle (measured using Btotal)-シア角。値が大きいと、自由エネルギーの大きさが大きい。\
                             <br> total unsigned flux-合計のフラックス。活動領域の大きさに近い。フラックスが増えているということは、磁力線が浮上し面積が増大しているということ。\
                             <br> 特に上2つが重要。確認すべきは値より傾向。増えている傾向があると注意。")

        },

        "Solar image": { **create_child_object("SDO Images", "https://sdo.gsfc.nasa.gov/data/", True, \
                        purpose="Confirmation of solar surface activity, coronal holes, CMEs and others", file_type="images", exampleVal="AIA 094's image is..., AIA 1700 image is...",\
                        memo = "SDO衛星による取得画像。波長ごとに見れるため、太陽表面の概観がエネルギーごとにわかる。 <br> 現在の太陽表面だけにとどまらず、1周期前を見るのも大事(特に極小期付近)。\
                            <br> 太陽の表面が1周期前と現在で近い模様をしている場合、1周期前に発生した事象を予報に活用できる(特にコロナホール)。\
                             <br> リンク先ページの左側一覧にある、AIA/HMI Browse Dataから画像や動画を探すとわかりやすい。\
                             <br> 主なもの： \
                                 <br> AIA 094 (green)-エネルギーがかなり高い。フレアの発生などがよく見える。また、チカチカ光ることもある(1600の説明参照)。\
                                 <br> AIA 211 (purple)-greenよりはエネルギーが低い。コロナホールが見えやすい。\
                                 <br> AIA 171 (gold)-エネルギー的にはgreenとpurpleの間。一番メジャーらしい。\
                                 <br>  &nbsp&nbsp;上3つに関してはCMEが見えることがある。(どの波長帯で一番よく見えるかはCMEの温度によって違う。335(blue)が一番良く見えるときもある。よく見える波長帯を探すのも大事。)\
                                 <br>  &nbsp&nbsp;このあたりのエネルギー帯で観測できるCMEは、コロナの放出を伴う。そのため、CMEが放出されるとき表面が暗くなる。(リム側だと吹き飛んでいく様子が見えることもある。)\
                                 <br>  &nbsp&nbsp;ただし、SDOの画像だけでCMEを判断するのは早計。必ずSOHOなどのコロナグラフ画像で、宇宙空間にプラズマが飛んでいく様子を確認すること。\
                                 <br> AIA 304 (red)-彩層がよく見える波長。フィラメントが太陽表面から飛んでいく様子が綺麗に見えるので、CMEが発生したかを確認するのに使える。(フィラメントが飛んでいたら、CMEが伴っている。) \
                                 <br> &nbsp&nbsp;注意すべきは、フレアが出ていてもCMEを伴っているかはわからないということ。また、コロナの放出がなくCMEがあることもある。(コロナは飛ばず、フィラメントだけ飛んでいるということ。)\
                                 <br> (フィラメントが飛んでいないけどコロナだけ飛んでいることもある。)\
                                 <br> &nbsp&nbsp;CMEを確認したい場合は304の確認も大事。もちろん、SOHOの確認は必須。\
                                 <br> AIA 1600 (yellow/green)-エネルギーが低め。彩層底部(光球上部)の光が見える。たまに、チカチカすることがある。このチカチカは AIA 094などでも見える。\
                                 <br> &nbsp&nbsp;チカチカの理由→黒点の下から浮上してきた磁場と、もともとの黒点が保持していた磁場がリコネクションを起こしてエネルギー開放を起こしている。\
                                 <br> 比較的小さいエネルギー解放なので、フレアと呼ばれるほどではないが、磁場の浮上がフレアのトリガーになることがある。\
                                 <br> &nbsp&nbsp;特にもともと大きい黒点に対して磁場が浮上してくると大きいフレアが生じることがあるため、磁場の浮上の確認は重要(=チカチカの確認は重要)。\
                                 <br> &nbsp&nbsp;なお、AIA 1600には遷移層の光も混じっているので注意。\
                                 <br> HMI Intensitygram-光球が見える。黒点がわかりやすい。 \
                                 <br> HMI Magnetogram-可視光による偏光観測。黒点の磁場構造が見える。この構造が複雑かつ大規模であるほど、大規模フレアが起きる傾向にある。\
                                 <br> &nbsp&nbsp;特に黒点画像(HMI Intensitygram)と比較することで、黒点がδ型か否かの判断が可能。\
                                 <br> HMI Colorized Magnetogram- Magnetogramのカラー版。モノクロは極性しか見えないが、カラー版は強度まで確認できる。\
                                 <br> \
                                 <br> 必ずしもどの波長かに拘る必要はなくて、現象が見やすいものを使うとよい。\
                                 <br> 波長ごとの画像のより詳しい説明はReference_URL参照 \
                                 <br> なお、The Sun Nowから見れる画像にはPFSSというバージョンがある。これは、Potential field source surfaceの略で、表面の磁場構造から太陽の磁場構造を推定したもの。\
                                 <br> PFSSから何かを言うのはかなりの知識が必要なようで、予報ではあまり使われない模様。また、Potentialから計算しているので、重要なはずの自由エネルギーが無視されていることにも注意。",\
                        refURL="https://aia.lmsal.com/public/instrument.htm"),

                        **create_child_object("SDO Images Dashboard", "https://sdo.gsfc.nasa.gov/data/dashboard/", True, \
                        purpose="Confirmation of solar surface activity, coronal holes, CMEs and others", file_type="images", \
                        memo = "SDO衛星による取得画像のダッシュボード版。見たい波長の画像を好きに並べられるので便利。 <br> 左上の歯車から好きな波長の画像を追加できる。 <br> Reference_URLに宇宙天気予報で使用頻度が高いものを並べたDashboardのリンクを添付。",\
                            refURL="https://sdo.gsfc.nasa.gov/data/dashboard/?d=0094;0211;0304;HMIBC;0193;1600;HMIIF;HMIB"),

                        **create_child_object("STEREO images", "https://stereo-ssc.nascom.nasa.gov/beacon/beacon_secchi.shtml", True, \
                        purpose="Images for Sun from different point", file_type= "images",\
                        memo="STEREO衛星による太陽の画像。SDOと違う場所を飛んでいるので、見えないところが気になる時に。 <br> ページの少し下のSDOの画像の中に混じっているSTEREO Aheadと書いてある画像も参考に使えるかも。(Aheadは衛星の名前なので、特に特別な意味はない。\
                                                    《もともとStereoはAheadとBehindの2機構成だった。Behindは壊れた。》)")

        },

        "Flare forecast by Deep Learning": create_child_object("Deep Flare Net", "https://defn.nict.go.jp/index131_eng.html", True, \
                                            purpose= "Forecast solar flare", file_type="text", \
                                            memo="深層学習を使って太陽フレアの発生率を予報しているサイト。フレアの「予報」の際の参考になる。\
                                             <br> DeFN - 平均的な発生頻度を50%とする。すなわち、50%を超えていたら、発生確率が「平均的な発生頻度より高い」とみなせる。つまり、50%を超えていても、「普段よりは起きやすい」だけ。\
                                             <br> DeFN-R - 実際のリアルな発生確率を予測している。すなわち、表示される確率と実際の発生頻度が等しい(20%だったら5回に1回ぐらい起きる)。確率予報には基本これ。\
                                             <br> DeFN-Q - XとMとCとNo-Flareの和が100%になるようにして表示している。(DeFN、DeFN-RはMクラス以上が起こる確率を示している。) \
                                             <br> DeFN-Rが確率予報として適切なので、DeFN-Rを使うべき。DeFNは空振りが多い。かわりに見逃しが少ない。DeFN-Qはまだα版のようなもので、リアルな発生確率を表していない。"),
    },
    
    "Proton flux": {
        "Proton flux": create_child_object("GOES Proton Flux", "https://www.swpc.noaa.gov/products/goes-proton-flux", True, \
                        purpose= "Present condition of solar energetic particles", file_type='graphs',exampleVal="10^0 particles/cm2/sec/sr前後、NOAAスケール S0",\
                        memo="Proton Fluxの変動を示す。Proton Fluxの変動は、Flux値をそのまま使って予報が出る事が多く、現況報告の意味合いが強い。\
                         <br> NOAAスケールとは、様々なイベントに対するNOAAが策定した指標。Proton fluxに関しては、桁数と一致(例えば、10^2を超えたらScale level S2)。<br> 詳しくはReference_URLのSolar Radiation Stormsタブを参照",\
                        refURL="https://www.swpc.noaa.gov/noaa-scales-explanation "),

    },

    "Solar wind": {
        "CME in space": { **create_child_object("SOHO LASCO C2 & C3", "https://soho.nascom.nasa.gov/data/Theater/", True, \
                        purpose="Confirmation of CME flying", file_type="images",\
                        memo="SOHOのコロナグラフを用いた観測機器LASCOによる動画。これにより、CMEがどのように宇宙空間に広がっていったかがわかる。 <br> SDOでは太陽表面の事象しか見れないので、これを見るのは重要。\
                         <br> サイトにアクセスした後、C2かC3を選び日程を設定してGenerate。C2とC3の違いは視野のみ。"),

                          **create_child_object("SOHO LASCO C2 & C3 Diff", "https://soho.nascom.nasa.gov/data/realtime/mpeg/", True, \
                        purpose="Confirmation of CME flying", file_type="images",\
                        memo="LASCOの動画でCMEを確認しようとした際、淡くてわかりにくいことがある。そこで、前の画像との差を表示するDiff版を使うと見やすくなる。 <br> サイトの下にあるLASCO C2 COMBOや、C3 COMBOがそれ。\
                             <br> なお、このサイトでは2日間の動画しか確認できない。数日前などを確認したい場合は、Reference_URLを使うと良い。 <br> ただし、主にC3が上手く表示されないことがある(サイトの問題ではなく、データ欠損のこともある。)\
                             <br> また、公式サイト(URLの方)のDailyという場所からアーカイブへ飛べる。しかし、現在の月より前のものしか見れないので注意。)")
                         
        },

        "L1 Solar wind": { **create_child_object("SWPC REAL TIME SOLAR WIND","https://www.swpc.noaa.gov/products/real-time-solar-wind", True, \
                            purpose="Confirmation of solar wind coming near the earth",file_type="graphs",exampleVal="Check these parameters at present condition and Previous rot (27days ago) : Solar source, Characteristics,Speed(620→520), Density(1前後), IMF(5nT前後、時折-6), Sector(概ねToward)",\
                            memo="SWPCが出している、DSCOVRとACEの観測データによるL1地点での太陽風データの時系列グラフ。基本的にはDSCOVRのデータで、抜けているデータをACEで補完している。 \
                             <br> 7daysにして見るのがおすすめ。 <br> また、一太陽周期前(27日前)のデータを見るのも良い。速度と磁場に関してはReference_URLの「27日太陽自転周期比較プロット」に27日前との比較プロットがある。",\
                            refURL="https://origin-swc.nict.go.jp/forecast/magnetosphere.html"),

                            **create_child_object("ACE REAL TIME SOLAR WIND", "https://www.swpc.noaa.gov/products/ace-real-time-solar-wind", True, \
                            purpose="Solar wind's high energy plasma",file_type="graphs",\
                            memo="ACEのリアルタイムの太陽風観測結果。右側にあるリストから、色々な観測機器のグラフが選べる。\
                             <br> EPAM(2桁keVから1桁MeVぐらいのプラズマ観測機器)とSIS(2桁MeVのプラズマの観測機器)のデータが特に大事。\
                             <br> (DSCOVRのほうがACEより新しいが、DSCOVRは高エネルギープラズマの観測機器が上手く行っていない。そのため、高エネルギープラズマに関してはACEのデータを見る必要がある。)")
        },

    },

    "Geomagnetic disturbances": {
        "Kp index": create_child_object("SWPC PLANETARY K-INDEX", "https://www.swpc.noaa.gov/products/planetary-k-index", True,\
                    purpose="Magnitude of geomagnetic disturbances across the globe",file_type="graphs",exampleVal="最大Kp指数:2.67(一日のうち最も大きいKp)  日合計値:13.66(3時間ごとに区切って出されるKpを、その日のもの全て(8つ)足す)  NOAA Scale: G0",\
                    memo="地球全体での地磁気擾乱の大きさを示す、Kp指数が見れる。(Kp index = Planetary K-index) \
                        <br> また、Kp指数をもとにした磁気擾乱に関するNOAAスケールもこのページに載っている。<br>スケールの説明はReference_URLのGeomagnetic Stormsタブに載っている。",\
                        refURL="https://www.swpc.noaa.gov/noaa-scales-explanation"),

        "K index": create_child_object("KAKIOKA K-INDEX", "https://origin-swc.nict.go.jp/trend/geomag.html",True,\
                    purpose="Magnitude of geomagnetic disturbance at Kakioka",file_type="graphs",exampleVal="最大K指数:3(一日のうち最も大きいKp)  日合計値:13(3時間ごとに区切って出されるKを、その日のもの全て(8つ)足す)  地磁気活動度: 静穏",\
                    memo="ローカルでの地磁気擾乱の大きさを示すK指数のうち、柿岡のものが見れる。日本での地磁気擾乱を考える際に重要。H componentは水平分力、D componentは偏角を表す。 \
                        地磁気活動度(Quiet, Active...)も載っている。地磁気活動度の基準はReference_URL参照。\
                        <br> 日合計値や各componentの詳細は https://www.kakioka-jma.go.jp/knowledge/glossary.html 参照", refURL="https://origin-swc.nict.go.jp/knowledge/criteria_icon.html"),

        "Simulation": create_child_object("SUSANOO", "https://cidas.isee.nagoya-u.ac.jp/susanoo/", True, \
                    purpose="Refer for forecast", file_type="graphs",\
                    memo="太陽風シミュレーションモデルSUSANOOによるL1地点での太陽風予報および、太陽系空間での太陽風予報。 <br> MHDシミュレーションらしい。 <br> nictのサイトのほうが見やすいかもしれない。(Reference_URL参照)",\
                    refURL="https://origin-swc.nict.go.jp/forecast/magnetosphere.html"),

        "Dst index": create_child_object("DST-INDEX", "https://wdc.kugi.kyoto-u.ac.jp/dstdir/index-j.html",True,\
                    purpose="DST-index",file_type="graphs",\
                    memo="DST指数。予報ではそんなに使わないのかも?"),

        "AE index": create_child_object("AE-INDEX", "https://wdc.kugi.kyoto-u.ac.jp/aedir/index-j.html",True,\
                    purpose="AE-index",file_type="graphs",exampleVal="None",\
                    memo="AE指数。予報ではそんなに使わないのかも?"),

    },

    "Radiation belts": {
        "Electron 24-h fluences": create_child_object("GOES Electron Fluences","https://origin-swc.nict.go.jp/trend/electron.html",True,\
                        purpose="Checking the electron 24-h fluences in the radiation belt", file_type="graphs",\
                        memo="GOESが取得した2MeV以上の電子fluxを、24時間で積分した値。GOESデータを元にNICTが積分した結果を出している。<br> 静止軌道衛星の観測データ24時間の総和なので、放射線帯全体の状況を表していると言える。\
                            <br> 放射線帯予報で重視すべきなのは、fluxよりもfluencesである。\
                            <br> 放射線帯全体の状況を表せることが主な理由。(Localな経度の情報を把握し発信することに重点を置いていない。)"),

        "Electron fluences forecast": create_child_object("電子フルエンス予報","https://radi.nict.go.jp/",True, \
                                        purpose="Reference for forecast electron fluences", file_type="text", \
                                        memo="放射線帯における24時間 Electron fluencesの、今後24時間、明日、明後日の予報。シミュレーションや統計モデルなど、複数のをもとに行われている。\
                                                <br> 予報の参考になる。静穏等々の基準についてはReference_URL参照",\
                                                    refURL="https://radi.nict.go.jp/about/#level"),
        
        "Electron flux": { **create_child_object("GOES Electron Flux","https://www.swpc.noaa.gov/products/goes-electron-flux",True,\
                            purpose="Checking the electron flux in the radiation belt", file_type="graphs",\
                            memo="GOESが取得した2MeV以上の電子fluxの時間変化。7daysで見るのが良さそう。\
                                <br> 現在の「GOESがいる経度」の放射線帯の電子fluxがわかる。グラフのNとMはNoonとMidnightの略で、衛星が昼側、夜側にいることを指す。\
                                <br> なお、GOES-16は西経75.2度、GOES-18は西経136.9度の静止衛星。 <br> 静止軌道は、平均的な放射線帯外帯の外端にあたる。"),

                            **create_child_object("GOES Electron Flux","https://himawari-seda.nict.go.jp/dataplot",True,\
                            purpose="Checking the electron flux in the radiation belt", file_type="graphs",\
                            memo="ひまわりが取得したMeV帯の電子fluxの時間変化。\
                                <br> 現在の「ひまわりがいる経度」の放射線帯の電子fluxがわかる。横軸はUTなので注意。\
                                <br> 上の設定を色々いじったあと、右上のPlotというボタンを押すとグラフが更新される。ひまわり8号、9号のデータが共に見れる。\
                                <br> ひまわりの経度は、8号9号ともにおよそ140.7度(0.05度離れているらしい。)。\
                                <br> 静止軌道は、平均的な放射線帯外帯の外端にあたる。")

        },
        
        "Electron flux forecast": create_child_object("静止軌道危険度予測","https://radi.nict.go.jp/satellite/",True,\
                purpose="Reference for forecast electron flux", file_type="graphs",\
                memo="シミュレーションや統計モデルによる電子fluxの時間変化の予測。 <br> ひまわり8号、GOES衛星それぞれの軌道における電子fluxの大きさの予報値が示されている。"),
    },

    "ionosphere": {
        "Sporadic E layer": { **create_child_object("Observed foEs","https://swc.nict.go.jp/trend/es.html",True,\
                                                purpose="Checking Sporadic E layer", file_type="graphs",\
                                                memo="Do it later"),

                              **create_child_object("Ionogram","https://swc.nict.go.jp/forecast/ionosphere.html",True,\
                                                purpose="Checking Sporadic E layer", file_type="graphs",\
                                                memo="国内イオノゾンデ定常観測の場所を参照 <br> Do it later")
        },

        "Ionospheric Storm": {
            **create_child_object("foF2 and GEONET TEC time change at Japan","https://swc.nict.go.jp/trend/ionosphere.html",True,\
                                  purpose="Checking ionospheric positive and negative storm", file_type="graphs",\
                                    memo="F層付近での電子密度(foF2)、上空の全電子密度(GEONET TEC)の変化を表す。どちらのデータも正相電離圏嵐、負相電離圏嵐の確認に使える。 <br> \
                                        foF2、GEONET TEC2つの違いはあまり注意しなくてよく、クロスチェックの意味合いが強い。"),

            **create_child_object("GEONET TEC map","https://aer-nc-web.nict.go.jp/GPS/QR_GEONET/",True,\
                                  purpose="Checking ionoshpheric storm",file_type="images",
                                  memo="日本上空の電子密度の空間分布を示したもの。日本のどの領域で電離圏嵐が発達しているかがわかる。")
        },
        
    },

    "Link collection site": {

        "NICT space weather forecast Trend": create_child_object("NICT Space Weather Forecast Trend","https://origin-swc.nict.go.jp/trend/",True,\
                                                           memo="各領域、各現象をクリックしたら関連グラフや数値と元データのリンクがすぐに出てくる。正直これで良い感ある。"),

        "NICT space weather forecast Link collection": create_child_object("NICT Space Weather Forecast Links","https://origin-swc.nict.go.jp/link/",True,\
                                                           memo="NICTの宇宙天気予報のサイトのリンク集。色々なサイトとか載ってる。"),

        "SOHO space weathers": create_child_object("SOHO Space Weather", "https://soho.nascom.nasa.gov/spaceweather/",True,\
                                                   memo="SOHOのサイトにあるリンク集。オーロラ予報とかシミュレーション予報とか載ってるの嬉しさがある。")
    }
}

# Save to a JSON file
with open("./Datas/space_weather_info.json", "w") as f:
    json.dump(space_weather_info, f, indent=4, ensure_ascii=False)

"/mnt/data/space_weather_info.json"
