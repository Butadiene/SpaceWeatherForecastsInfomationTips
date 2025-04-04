import json

# 情報リストのベタ書き

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

    "Space weather forecast reports": {
        "List of space weather forecast for each country": create_child_object("Present Space Weather Forecast from ISES", "https://swc.nict.go.jp/data/ises/isesforecast.html", True,\
                                                                purpose="Check space weather forecast for each country",file_type="text",\
                                                                memo="ISES(The International Space Environment Service)のメンバー国が出している宇宙天気予報を一覧で見られる。\
                                                                    <br> なお、各国の詳細なレポートはRefence_URL参照。", refURL="http://www.spaceweather.org/ISES/discussion/LatestForecast.jsp#ad-image-24"),

        "NICT Space Weather Forecast Report": create_child_object("NICT 宇宙天気予報レポーㇳ", "https://swc.nict.go.jp/report/", True,\
                                                                purpose="Check space weather forecast reports, especially daily report",file_type="text",\
                                                                memo="NICTが出している宇宙天気予報のレポーㇳ。特に日報はその日の現象がよくまとまっており、参照すべきである。"),
    },

    "Solar and geophysical events": {
        "All event reports (SWPC)": create_child_object("SWPC SOLAR AND GEOPHYSICAL EVENT REPORTS","https://www.swpc.noaa.gov/products/solar-and-geophysical-event-reports",True,\
                                purpose="Check events list",file_type="text",\
                                    memo="太陽表面や磁気圏でのイベントのリスト。日付ごとのリストになっている。主要なイベントのリスㇳになっていて重要。\
                                         <br> SWPC(Space Weather Prediction Center)から出されたリスト。\
                                         <br> BeginとEndがイベント発生と終了時間。Maxがピークタイム。Maxのタイムをイベント時刻として採用することが多い。\
                                         <br> X線観測の結果のイベント、光学観測結果のイベント等々をすべて別物として扱う。どの観測手法で、どのように検知されたかをTypeが示す。\
                                         <br> なお、異なる機器で観測されたイベントが同じ現象によって生じたものと判断した場合、同じイベント番号を振る。\
                                         <br> \
                                         <br> サイトの少し下のDetailsのところにあるリンクからType一覧を確認できる。 <br> 例：ftp://ftp.swpc.noaa.gov/pub/indices/ にアクセスし、eventsフォルダの中のREADMEを確認。\
                                         <br> また、過去のデータはftpでテキストファイルでしか配布されていない。サイトの少し下のDataのところにあるリンクから、過去のデータをダウンロードできる。\
                                         <br> 例：ftp://ftp.swpc.noaa.gov/pub/indices/ にアクセスし、eventsフォルダの中のテキストファイルを確認。"),

        "Last flare event reports (LMSAL)": create_child_object("LMSAL last event reports","https://www.lmsal.com/solarsoft/last_events/",True,\
                                purpose="Check events list",file_type="text",\
                                    memo="フレアのイベントのリスト。直近20イベントのリストになっている。 <br> 直近20イベントだけだが、NOAAのものと違ってリストで示されていたり、図もついていたりと見やすい。 <br> イベント時刻はピークタイムを使う事が多い。\
                                        <br> なお、20件より前のイベントはrefURLから辿れる模様。結構なところまで遡れるっぽい。", refURL="https://www.lmsal.com/solarsoft/latest_events_archive.html"),
        
        "A Heliophysics Events Knowledgebase": create_child_object("A Heliophysics Events Knowledgebase to facilitate scientific discover","https://www.lmsal.com/isolsearch",True,\
                                    purpose="Check events list",file_type="images",\
                                        memo="フレア、CME、コロナホール、フィラメント、コロナホール、黒点、紫外線イベントなどのほぼ全てのイベントを網羅し、マッピングしているサイト。全イベントの詳細も載っている。。\
                                            <br> 特にすごいのはCMEやフィラメント、フィラメント噴出イベントのリストがある他、フレアについてはGOES Xray-fluxで補足できていないものもSDOの画像から推定している。\
                                            <br> アルゴリズムで検出してるだけであるっぽいのでそこは注意。左側の選択バーで現象と時期選んでsearchをクリック。またAPIも充実している。\
                                            <br> 主な扱ってる現象リストはreference_URL参照。api情報や検出ソフトについてはrefURL2参照。", refURL="https://www.lmsal.com/hek/VOEvent_Spec.html", refURL2="https://www.lmsal.com/hek/api.html"),
    
    },

    "All graphs": {
        "All graphs of spaceweather": create_child_object("Space weather portal", "https://lasp.colorado.edu/space-weather-portal/", True,\
                                        purpose="Check all graphs of spaceweather", file_type="graphs", \
                                        memo="宇宙天気に関するグラフがまとめられているサイト。太陽風のグラフや地磁気の乱れのグラフなどを、任意の期間まとめてプロットすることが可能。\
                                            <br> さらに、データをアウトプットすることも可能。\
                                            <br> 使い方は、Dataタブを開いた後、期間を指定。その後、プロットしたいデータを選択してDisplay。\
                                            <br> なお複数のグラフを一つの図の中にプロットしたい場合は、プロットしたグラフの左側にあるギザギザのアイコン「Edit datasets and variables」から設定可能。\
                                            <br> データのアウトプットはDownloadタブから行うことが可能。"),
    },

    "Solar flares": {
        "X-ray flux": create_child_object("GOES X-ray Flux", "https://www.swpc.noaa.gov/products/goes-x-ray-flux/", True, \
                    purpose="GOES background X-ray flux",file_type="graphs", exampleVal="B7, 穏やかに上昇中", \
                    memo="GOES衛星が捉えた太陽からのX線の量。太陽活動の重要な指標。 <br> グラフにマウスを当てると、値が表示される。赤やオレンジのGOES-16 long, GOES-18 longの値がフレアのクラスとして採用されている模様。\
                        <br> 尖っているところがフレアが起きているところとされ、要注目。尖っているところのピークの値がフレアのクラスになる。\
                        <br> \
                        <br> ピーク以外にも尖り方の「形」にも注意する必要がある。X-ray fluxがフレアで急激に上昇すると、その後すみやかに減少する事が多い。 \
                        <br> しかし、減少速度が緩やか(数時間から長いものだと1日以上)なものがあり、これをLDE(Long Duration Event)と呼ぶ。\
                        <br> LDEはCMEを伴うことが多いことで知られているため、特に注意すべきフレアイベントである。\
                        <br> \
                        <br> フレアが起きていない（≒尖っていないところ）の値をバックグラウンドと呼んだりする。\
                        <br> これも重要で、バックグラウンドが上昇傾向にある場合は、例えば東側から活動的な領域が見え始めていたりすることを意味する可能性がある。"),
                        
        "Radio flux": {**create_child_object("Solar radio flux - archive of measurements", "https://www.spaceweather.gc.ca/forecast-prevision/solar-solaire/solarflux/sx-5-en.php", True,\
                            purpose="F10.7: 10.7cm wavelength radio wave strength", file_type="html", \
                            memo="太陽黒点数と良い相関のある、波長10.7cm(周波数2.8GHz)の電波の強度。 <br> Daily flux valuesのHTML見れば良いけど、\
                            めちゃ見づらいので注意。値はObserved fluxを使用すると良さそう。 <br> 極大期では月平均でおおよそ200、極小期では70程度(日単位では変動が大きく、300を超えることも。)\
                                <br> DRAO(Dominion Radio Astrophysical Observatory research facility)による。"),

                        **create_child_object("NICT Solar Observation Database","https://solarobs.nict.go.jp/", True, \
                            purpose= "Solar radio burst", file_type="graphs", \
                            memo="NICTが行っている太陽の観測データが見れる。\
                                 <br> 使う可能性が大きいのは山川での太陽電波観測結果(Real-time dynamic spectrum of YAMAGAWA solar radio spectrograph)。\
                                 <br> 太陽電波バーストなどを見るのに良い。\
                                 <br> 太陽電波バーストは太陽活動を示すイベントとして重要だが、山川の観測データからイベントを識別するのは難しく、初心者向けではない。")

        },

        "Synoptic analysis": create_child_object("SOLAR SYNOPTIC MAP","https://www.swpc.noaa.gov/products/solar-synoptic-map", True, \
                                                  purpose="Assessing the conditions on the sun", file_type="images", 
                                                  memo="SWPCの宇宙天気予報担当者が太陽表面についての解析を行い、それを描いたもの。\
                                                    <br> 1日に1~2回更新されている。\
                                                    <br> 人の手を介することで様々な判断がなされ、結果が書き込まれている。\
                                                    <br> \
                                                    <br> 特に、コロナホールと磁場極性を見ることができるのが便利。\
                                                    <br> 実線で囲まれ、かつ境界線に短いたくさんの線が内向きについている場所が、予報担当者がコロナホールと判断した場所である。\
                                                    <br> また、その内部に太陽表面での磁場極性が記載されている。よって予報担当者が\
                                                    <br>「どこにコロナホールがあり、コロナホール内部にあたる領域にて、太陽表面では磁場極性が正か負か」\
                                                    <br> を判断したかがわかる。\
                                                    <br> 極性については、特に正負が重要。\
                                                    <br> なお、正負記号の右隣に書いてあるのはコロナホール解析の信頼度(4がmaxで1が最低)である。\
                                                    <br> \
                                                    <br> 各活動領域については領域の番号に加え、今後24時間以内にフレアやプロトン現象が発生する確率が書いてあり、参考になる。\
                                                    <br> 番号の下に C/M/X/Pの順番で記載されている。(Cクラスフレア、Mクラスフレア、Xクラスフレア、プロトンイベントの生じる確率)\
                                                    <br> \
                                                    <br>下のDetailsに見方が載っている。また、Dataのところからアーカイブにアクセスできる。\
                                                    <br>アーカイブは昨日のものから見ることができ、非常にアクセスしやすいものとなっている。"\
                                                    ),

        "Sun spot": {**create_child_object("SILSO : Daily estimated sunspot number", "https://www.sidc.be/SILSO/home", True, \
                      purpose= "Relative sunspot number", file_type="text", exampleVal="109, 一定", \
                      memo="太陽黒点相対数。太陽光球面に出現する黒点および黒点群の総数を数値化したもの。サイトのホームの右端にある。"),

                    **create_child_object("SILSO : Monthly relative sunspot number", "https://www.sidc.be/products/ri/", True, \
                      purpose= "Monthly relative sunspot number", file_type="text", exampleVal="Result: Jul-23 159.1   Forecast: Aug-23 154, Sep-23 160", \
                      memo="太陽黒点相対数の月平均。予測値も見れる。月平均の値なので、一月に一回しか更新されない。"),
            
            
                    **create_child_object("SOLAR REGION SUMMARY", "https://www.swpc.noaa.gov/products/solar-region-summary", True, \
                        purpose="Sunspot area (SWPC) & Charactistics of active regions", file_type="text", exampleVal="Sunspot area:660, 穏やかに上昇中 & Charactistics of active regions:領域、位置、面積...", \
                        memo="現在の太陽黒点の一覧とその性質が載っている。SRSと略され、重要なデータの一つ。 \
                            <br> 現在の黒点の総面積を出したいときは、SRSに載っている黒点の面積をすべて足す。\
                            <br> 各項目の簡単な説明\
                            <br> Z- Modified Zurich classification of the group. 修正チューリッヒクラス。3つのアルファベットの組み合わせで表される。Reference_URL参照\
                            <br> Lo- Carrington longitude of the group.\
                            <br> LL- Longitudinal extent of the group in heliographic degrees.\
                            <br> NN- Total number of visible sunspots in the group.\
                            <br> Mag Type- Magnetic classification of the group. マウント・ウィルソン分類による黒点の分類。α、β、βγ、γ、δなどがあり、δに行くほどフレアを起こしやすいとされる。\
                            <br> &nbsp&nbsp;δ型にだけ要警戒しておけばとりあえずは良い。\
                            <br> &nbsp&nbsp;以下に簡単に説明。詳しくはReference_URL2参照。\
                            <br> &nbsp&nbsp;&nbsp;&nbsp;α：単極で存在するもの。\
                            <br> &nbsp&nbsp;&nbsp;&nbsp;β：2つの極から成る単純な黒点の対。つまり、2つの黒点が近くにあり、その2つの極性が逆(NとSになっている)。\
                            <br> &nbsp&nbsp;&nbsp;&nbsp;γ：β には分類しがたいような複雑な極構造を持った黒点。\
                            <br> &nbsp&nbsp;&nbsp;&nbsp;δ：2つの黒点が近くにあり、その2つの極性が逆。かつ2つの黒点は半暗部を共有している。すなわち、半暗部の中に2つの暗部があり、その2つの極性が逆になっている。一番コロナが起きやすい。\
                            <br> \
                            <br> その黒点がいつから発生したかを知りたいときは、過去のデータを参照すると良い。\
                            <br> なお、過去のデータはftpでテキストファイルでしか配布されていない。サイトの少し下のDataのところにあるリンクから、過去のデータをダウンロードできる。 <br> 例：ftp://ftp.swpc.noaa.gov/pub/forecasts/ にアクセスし、SRSフォルダの中のテキストファイルを確認",\
                                refURL="https://www.spaceweatherlive.com/en/help/the-classification-of-sunspots-after-malde.html",\
                                refURL2="https://solarphys.com/dynamics/ar/"),
                        
                    **create_child_object("SOHO Sunspots", "https://soho.nascom.nasa.gov/sunspots/", True, \
                        purpose= "Check sunspot numbers with sunspot images", file_type="images", 
                        memo= "SOHOの白黒光球画像。黒点が番号付きで表示されるのが便利。"),

                     **create_child_object("SHARP Vector Magnetograms", "https://defn.nict.go.jp/sharp/index_sharp_jp.html",True,\
                        purpose="Check degree of magnetic field distortion (shear)", file_type="images",\
                        memo="各黒点の磁場の歪み具合を画像でわかりやすく示してくれる。 <br> この構造が複雑であれば（具体的には極性が複雑でかつコンパクトにまとまった黒点）、より大きいフレアを警戒する必要がある。 \
                            <br> 特に確認すべきはシア。赤色(水平磁場)の矢印が、緑色の線(磁気中性線)と平行かつ緑色の線を挟んで逆方向になっている場合（シアという）、よりフレアを警戒する必要がある。 <br> (緑色の断層線に沿って赤方向にずれる横ずれ断層をイメージすると良いかも。)\
                            <br> 逆に、磁気中性線と水平磁場の向き(赤色の矢印)が直交しているときは、シアがあまりないと言えるので、そこまで警戒の必要がない可能性がある。\
                            <br> 英語版はReference_URLに記載。", refURL="https://defn.nict.go.jp/sharp/index_sharp.html"),

                     **create_child_object("SHARP Data Viewer", "http://jsoc.stanford.edu/data/hmi/sharp/dataviewer/",True,\
                        purpose="Check degree of magnetic field distortion (shear)", file_type="images",\
                        memo="シアやフラックスの値などを定量的に示したのが SHARP Data Viewer。\
                             <br> 右上のsettingsから表示項目が設定できる。以下の2つをよく使う。\
                             <br> &nbsp&nbsp;mean shear angle (measured using Btotal)-シア角。値が大きいと、自由エネルギーの大きさが大きい。\
                             <br> &nbsp&nbsp;total unsigned flux-合計のフラックス。活動領域の大きさに近い。フラックスが増えているということは、磁力線が浮上し面積が増大しているということ。\
                             <br> 確認すべきは値より傾向。増えている傾向があると注意。"),
                    
                    **create_child_object("Far side sunspot images", "https://farside.nso.edu/", True, \
                                          purpose="Check far side sunspot images", file_type="images", \
                                            memo="太陽の裏側の黒点の推定画像。GONGという太陽の観測ネットワークから提供された、太陽での振動の表面速度の計測値を用いて推定しているらしい(全然わからない)。\
                                                <br> 黒点の回り込みに関する議論をしたいときに参考程度に。\
                                                    <br> ReferenceURLは推定方法に関して",\
                                                        refURL="https://farside.nso.edu/more_info.html")

        },

        "Solar image": { **create_child_object("SDO Images", "https://sdo.gsfc.nasa.gov/data/", True, \
                        purpose="Confirmation of solar surface activity, coronal holes, CMEs and others", file_type="images", exampleVal="AIA 094's image is..., AIA 1700 image is...",\
                        memo = "SDO衛星による取得画像。波長ごとに見れるため、太陽表面の概観がエネルギーごとにわかる。 \
                            <br> 現在の太陽表面だけにとどまらず、3-4日前までは必ず確認すべき。なぜなら、CMEは高速太陽風は太陽表面での事象から一般に3-4日遅れて地球に影響を及ぼすため。\
                            <br> また、1太陽周期前を見るのも大事(特に極小期付近)。\
                            <br> 太陽の表面が1周期前と現在で近い模様をしている場合、1周期前に発生した事象を予報に活用できる(特にコロナホールによる高速太陽風)。\
                            <br> \
                             <br> リンク先ページの左側一覧にある、AIA/HMI Browse Dataから画像や動画を探すとわかりやすい。\
                             <br> なおBrowse Dataから見る場合、解像度は1024より512のほうがおすすめ。(1024は上手く動かないことが多い。)\
                             <br> 主なもの： \
                                 <br> AIA 094 (green)-エネルギーがかなり高い。フレアの発生などがよく見える。また、チカチカ光ることもある(AIA 1600の説明参照)。\
                                 <br> &nbsp&nbsp;フレアの発生の際は、黒点領域のどのあたり(黒点の南側か、北側かなど)で発生したかまで意識できると良い。発生領域が細かくわかると、磁場構造の確認の際の助けになる。\
                                 <br> \
                                 <br> AIA 211 (purple)-greenよりはエネルギーが低い。コロナホールが見えやすい。AIA 211で黒い穴(点ではなくはっきりとわかる穴)があったらコロナホールの可能性。 \
                                 <br> &nbsp&nbsp;大きいコロナホールはより注視する必要がある。(大きいとは、地球から見た太陽表面直径の1/5くらいの直径を持ったホールを指すっぽい?)\
                                 <br> &nbsp&nbsp;そこそこ小さくても、はっきりわかる黒い穴があったらコロナホールを疑ってみるのは大事。\
                                 <br> &nbsp&nbsp;コロナホールから飛び出す高速太陽風は太陽半径方向に飛んでいく傾向がある。そのためコロナホールがあった場合、コロナホールが子午線にいる日時を認識すると良い。\
                                 <br> &nbsp&nbsp;高速太陽風の速度は500km/s以上であることが多いため、コロナホールが子午線にいる日時から3-4日後に高速太陽風到来の可能性が高い。現在から3-4日前までの画像を確認するのが大事。\
                                 <br> &nbsp&nbsp;また、より低緯度帯にいるコロナホールほど着目する必要がある。\
                                 <br> \
                                 <br> AIA 171 (gold)-エネルギー的にはgreenとpurpleの間。一番メジャーらしい。\
                                 <br> \
                                 <br> AIA 094、211、171あたりの波長帯の画像では、CMEが見えることがある。\
                                 <br> &nbsp&nbsp;このあたりの波長帯で観測できるCMEは、コロナの放出を伴う。そのため、CMEが放出されるとき表面が暗くなる様に見える。(Dimmingと呼ばれる)\
                                 <br> &nbsp&nbsp; (リム側だと吹き飛んでいく様子が見えることもある。)\
                                 <br> &nbsp&nbsp;(CMEが どの波長帯で一番よく見えるかは、そのときのCMEの温度によって違う。335(blue)が一番良く見えるときもある。よく見える波長帯を探すのも大事。)\
                                 <br> &nbsp&nbsp;ただし、SDOの画像だけでCMEを判断するのは早計。必ずSOHOのLASCOなどによるコロナグラフ画像で、宇宙空間にプラズマが飛んでいく様子を確認すること。\
                                 <br> &nbsp&nbsp;また、CMEは地球に到来するまで数日かかる。そのため、CMEに関する判断をする際は、4日前までのSDO画像をちゃんと確認する。\
                                 <br> \
                                 <br> AIA 304 (red)-彩層がよく見える波長。フィラメントが太陽表面から飛んでいく様子が綺麗に見えるので、CMEが発生したかを確認するのに使える。(フィラメントが飛んでいたら、CMEが伴っている。) \
                                 <br> &nbsp&nbsp;CMEは常にコロナの放出とフィラメントの放出の両方を伴うわけではなく、片方のみのこともある。\
                                 <br> &nbsp&nbsp;そのためCMEを確認したい場合は、上で述べたエネルギーが高い波長帯によるコロナの吹き飛びの確認と、AIA 304によるフィラメントの吹き飛びの確認の両方が大事。\
                                 <br> &nbsp&nbsp;またフレアが出ていてもCMEを伴っていないこともあれば、フレアが出ていなくてもCMEが起きていることもある。よって、フレアイベントと関係なく確認するべき。\
                                 <br> &nbsp&nbsp;もちろん、SOHOのLASCOなどによるコロナグラフデータの確認は必須。\
                                 <br> \
                                 <br> AIA 1600 (yellow/green)-エネルギーが低め。彩層底部(光球上部)と遷移層が見える。たまに、チカチカすることがある。このチカチカは AIA 094などでも見える。\
                                 <br> &nbsp&nbsp;チカチカはフレアによって起きるもの(遷移層の光を見ている)と、黒点の下から磁場が浮上して起きるもの(彩層底部(光球上部)の光を見ている)がある。(もちろん例外もある。)\
                                 <br> &nbsp&nbsp;浮上磁場について: 黒点の下から浮上してきた磁場と、もともとの黒点が保持していた磁場がリコネクションを起こしてエネルギー開放を起こしている。\
                                 <br> &nbsp&nbsp;&nbsp&nbsp;比較的小さいエネルギー解放なので、フレアと呼ばれるほどではないが、磁場の浮上がフレアのトリガーになることがある。\
                                 <br> &nbsp&nbsp;&nbsp&nbsp;特にもともと大きい黒点に対して磁場が浮上してくると大きいフレアが生じることがあるため、磁場の浮上の確認は重要(=チカチカの確認は重要)。\
                                 <br> &nbsp&nbsp;&nbsp&nbsp;具体的には、「磁場浮上が頻繁に起きていて、それに伴い黒点の磁場構造も変化するなど活発な活動が見える。」といった検討が行える。\
                                 <br> &nbsp&nbsp;ただしチカチカはフレアによって生じていることもあるので、チカチカの確認を行う際はフレアイベントとの突き合わせの際も同時に行う必要あり。\
                                 <br> \
                                 <br> HMI Intensitygram-光球が見える。黒点がわかりやすい。 \
                                 <br> \
                                 <br> HMI Magnetogram-可視光による偏光観測。黒点の磁場構造が見える。この構造が複雑かつ大規模であるほど、大規模フレアが起きる傾向にある。\
                                 <br> &nbsp&nbsp;特に黒点画像(HMI Intensitygram)と比較することで、黒点がδ型か否かの判断が可能。\
                                 <br> \
                                 <br> HMI Colorized Magnetogram- Magnetogramのカラー版。モノクロは極性しか見えないが、カラー版は強度まで確認できる。\
                                 <br> \
                                 <br> 必ずしもどの波長かに拘る必要はなくて、現象が見やすいものを使うとよい。\
                                 <br> 波長ごとの画像のより詳しい説明はReference_URL参照 \
                                 <br> \
                                 <br> なおリンク先サイトの左側一覧にあるThe Sun Nowから見れる画像には、PFSSというバージョンがある。これは、Potential field source surfaceの略で、表面の磁場構造から太陽の磁場構造を推定したもの。\
                                 <br> PFSSから何かを言うのはかなりの知識が必要なようで、予報ではあまり使われない模様。また、Potentialから計算しているので、重要なはずの自由エネルギーが無視されていることにも注意。",\
                        refURL="https://sdo.gsfc.nasa.gov/data/channels.php"),

                        **create_child_object("SDO Images Dashboard", "https://sdo.gsfc.nasa.gov/data/dashboard/", True, \
                        purpose="Confirmation of solar surface activity, coronal holes, CMEs and others", file_type="images", \
                        memo = "SDO衛星による取得画像のダッシュボード版。見たい波長の画像を好きに並べられるので便利。 <br> 左上の歯車から好きな波長の画像を追加できる。\
                             <br> ただし、最新の動画が載っていないことがある。Browse Dataから検索して得た動画に比べて数時間から10時間ほど遅かったりもすることもあるので注意。\
                             <br> Reference_URLに宇宙天気予報で使用頻度が高いものを並べたDashboardのリンクを添付。",\
                            refURL="https://sdo.gsfc.nasa.gov/data/dashboard/?d=0094;0211;0304;HMIBC;0193;1600;HMIIF;HMIB"),

                        **create_child_object("STEREO images", "https://stereo-ssc.nascom.nasa.gov/beacon/beacon_secchi.shtml", True, \
                        purpose="Images for Sun from different point", file_type= "images",\
                        memo="STEREO衛星による太陽の画像。SDOと違う場所を飛んでいるので、見えないところが気になる時に。(ただし、2023年はSOHOと同じ場所を飛んでいる...。) <br> ページ内で表示されている360度画像や、STEREO Aheadと書いてある画像がそれ。\
                                <br> (Aheadは衛星の名前なので、特に特別な意味はない。《もともとStereoはAheadとBehindの2機構成だった。Behindは壊れた。》)"),
                        
                        **create_child_object("Solar Monitor", "https://www.solarmonitor.org/", True, \
                                              purpose="Confirmation of solar surface activity, coronal holes, CMEs and others", file_type="images", \
                                                memo="SDOの画像や活動領域とその番号、コロナホールの位置などをまとめたサイト。 \
                                                    <br> 一覧性が高く、見やすい。 \
                                                    <br> 特に、コロナホールの位置を確認するのに便利。(コロナホールの判定をするのは難しいので)\
                                                    <br> 左側のCoronal Holesから見れる。\
                                                    <br> コロナホール確認画面では、画像にてコロナホールと推定される領域が図示されている。画像の下の表には各領域のプロパティが書いてある。\
                                                    <br> 表で特に重要なのは、コロナホール内部の領域における、太陽表面での磁場極性である。(表におけるBに相当)\
                                                    <br> コロナホール内部領域での太陽表面での磁場極性は、+か-かが特に重要。\
                                                    <br> また、1太陽周期前の画像がすごく見やすくなっている。(左上のRotationから選択)")

        },

        "Flare forecast by Deep Learning": create_child_object("Deep Flare Net", "https://defn.nict.go.jp/index131_rel_eng.html", True, \
                                            purpose= "Forecast solar flare", file_type="text", \
                                            memo="深層学習を使って太陽フレアの発生率を予報しているサイト。フレアの「予報」の際の参考になる。\
                                             <br> \
                                             <br> DeFN - 平均的な発生頻度を50%とする。すなわち、50%を超えていたら、発生確率が「平均的な発生頻度より高い」とみなせる。つまり、50%を超えていても、「普段よりは起きやすい」だけ。\
                                             <br> DeFN-R - 実際のリアルな発生確率を予測している。すなわち、表示される確率と実際の発生頻度が等しい(20%だったら5回に1回ぐらい起きる)。確率予報には基本これ。\
                                             <br> DeFN-Q - XとMとCとNo-Flareの和が100%になるようにして表示している。(DeFN、DeFN-RはMクラス以上が起こる確率を示している。) \
                                             <br> \
                                             <br> リンク先はDeFN-Rのものにしてある。上のメニューから切り替えできる。\
                                             <br> DeFN-Rが確率予報として適切なので、DeFN-Rを使うべき。DeFNは空振りが多い。かわりに見逃しが少ない。DeFN-Qはまだα版のようなもので、リアルな発生確率を表していない。"),
    },

    "All Solar datas":{
        "Virtual Solar Observatory": create_child_object("Virtual Solar Observatory", "https://sdac.virtualsolar.org/cgi/search", True, \
                                                         purpose="All Solar Observatories", file_type="images",\
                                                            memo="いろんな太陽衛星観測のデータをまとめたサイト\
                                                                <br>1. Please select which values you wish to use to search for data productsで機器が観測可能か,\
                                                                <br>, Instrument/Provider, Spectral Range (電波長, UVなど), Nicknames がある. どれかを選択し, Generate VSO Search Form を押せばそれに合った観測機器・データが示される．\
                                                                <br>2. 衛星やその機器を選ぶ. Date Rangeに注意. \
                                                                <br>3. 右上にStartとEndがプルダウンで表示されるので, ほしいデータの時間帯を選択し, Searchを押す\
                                                                <br>4. データがない場合はエラーが出る．取得したいデータの時間帯を選択．\
                                                                <br>5. Image linkを押せば写真を取得できる. 生データを取得したい場合は左のRequest Dataを押す. \
                                                                <br>6. URL-TAR, URL-FILE, URL-FILE_Riceなどがある. 無難にURL-FILEでいいと思う.\
                                                                <br>7. URLが出てくるので押せばダウンロードが始まる. \
                                                                "),
    },
    
    "Proton flux": {
        "Proton flux": create_child_object("GOES Proton Flux", "https://www.swpc.noaa.gov/products/goes-proton-flux", True, \
                        purpose= "Present condition of solar energetic particles", file_type='graphs',exampleVal="10^0 particles/cm2/sec/sr前後、NOAAスケール S0",\
                        memo="MeV帯以上のProton Fluxの変動を示す。プロトン現象の把握に使える。\
                         <br> NOAAスケールとは、様々なイベントに対するNOAAが策定した指標。Proton fluxに関しては、桁数と一致。(例えば、10^2を超えたらScale level S2) <br> 詳しくはReference_URLのSolar Radiation Stormsタブを参照。\
                         <br> Proton Fluxの予報はFluxの観測値をそのまま使って出す事が多く、現況報告の意味合いが強くなりがちである。",\
                        refURL="https://www.swpc.noaa.gov/noaa-scales-explanation "),

    },

    "Radio flux (Solar radio burst)": {
        
                        "Radio flux":{
                            **create_child_object("Solar radio flux - archive of measurements", "https://www.spaceweather.gc.ca/forecast-prevision/solar-solaire/solarflux/sx-5-en.php", True,\
                            purpose="F10.7: 10.7cm wavelength radio wave strength", file_type="html", \
                            memo="太陽黒点数と良い相関のある、波長10.7cm(周波数2.8GHz)の電波の強度。 <br> Daily flux valuesのHTML見れば良いけど、\
                            めちゃ見づらいので注意。値はObserved fluxを使用すると良さそう。 <br> 極大期では月平均でおおよそ200、極小期では70程度(日単位では変動が大きく、300を超えることも。)\
                                <br> DRAO(Dominion Radio Astrophysical Observatory research facility)による。"),
                        },

                        "Solar radio burst":{

                            **create_child_object("NICT Solar Observation Database","https://solarobs.nict.go.jp/", True, \
                            purpose= "Solar radio burst", file_type="graphs", \
                            memo="NICTが行っている太陽の観測データが見れる。\
                                 <br> 使う可能性が大きいのは山川での太陽電波観測結果(Real-time dynamic spectrum of YAMAGAWA solar radio spectrograph)。\
                                 <br> 太陽電波バーストなどを見るのに良い。\
                                 <br> 太陽電波バーストは太陽活動を示すイベントとして重要だが、山川の観測データからイベントを識別するのは難しく、初心者向けではない。"),

                         **create_child_object("e-callisto", "http://soleil.i4ds.ch/solarradio/callistoQuicklooks/", True, \
                            purpose="Confirmation of solar radio burst", file_type="images",\
                                memo="太陽電波バーストの観測データ。世界各地（地表）で観測された、様々な周波数帯での観測結果が見れる。<br> \
                                太陽活動に伴って様々な型のバーストが発生していることを確認することができる。特に太陽フレアやCMEについて検討する際の指標になる。<br> \
                                日付を指定して、見たい観測点と時間帯のデータのImageとある文字にマウスカーソルを重ねると、スペクトルデータが表示される。<br>\
                                Imageをクリックすると拡大画像が表示される。Fitsをクリックするとzipファイルがダウンロードされる。<br>\
                                Reference_URLより、各観測点と、その観測点で観測できる周波数帯のデータが確認できる。<br>\
                                Reference_URL2には、e-callistoのトップページを記載。<br>\
                                各月のバースト検出数の総計が見たい場合は、<br>\
                                https://www.e-callisto.org/Data/BurstCountsYYYYMM.png のYYYYMMを編集してアクセスすると良い。",
                                refURL="https://soleil.i4ds.ch/solarradio/data/readme.txt", refURL2="https://www.e-callisto.org/")
                        },

        },

    "Solar wind": {

        "L1 Solar wind": { **create_child_object("SWPC REAL TIME SOLAR WIND","https://www.swpc.noaa.gov/products/real-time-solar-wind", True, \
                            purpose="Confirmation of solar wind coming near the earth",file_type="graphs",exampleVal="Check these parameters at present condition and Previous rot (27days ago) : Solar source, Characteristics,Speed(620→520), Density(1前後), IMF(5nT前後、時折-6), Sector(概ねToward)",\
                            memo="SWPCが出している、DSCOVRとACEの観測データによるL1地点での太陽風データの時系列グラフ。 \
                             <br> 太陽風が高速であるか(具体的には500km/s以上)、磁場が強くかつ南向きを示しているか、密度上昇があるか、などが重要な確認点。\
                             <br> デフォルトでは磁場データの左側に<s>Bx</s>の様なラベルが見えると思うが、クリックするとBxのグラフも表示されるようになる。(Byも同様)\
                             <br> Phi GSMは磁場が地球方向に向いているか、太陽方向に向いているかについての角度。地球方向に向いている場合はAway(+)、太陽方向を向いている場合はTowards(-)と呼んだりする。\
                             <br> 7daysにして見るのがおすすめ。 <br> また、一太陽周期前(27日前)のデータを見るのも良い。速度と磁場に関してはReference_URLのリンク先ページの下の方に「27日太陽自転周期比較プロット」に27日前との比較プロットがある。\
                             <br> グラフの下にあるSeriesから、グラフを切り替えられる。特に、データ元衛星の切り替えは頭に入れる必要がある。\
                             <br> 過去データを見たい場合は、期間を1yearやAllなどにして見たい期間を表示した後に、SeriesタブのZoon機能を使うと良い。\
                             <br> なお、グラフをマウスでドラッグすることによるズームインアウトも可能。\
                             <br> &nbsp&nbsp; Active spacecraft (デフォルト): 基本的にはDSCOVRのデータで、抜けているデータをACEで補完している。\
                             <br> &nbsp&nbsp; DSCOVR only: DSCOVRのデータのみ\
                             <br> &nbsp&nbsp; Ace only: Aceのデータのみ\
                             <br> Active spacecraftやDSCOVR onlyのデータが大きく乱れていたりする時、Ace onlyでも確認してみると良い。",\
                            refURL="https://origin-swc.nict.go.jp/forecast/magnetosphere.html"),

                            **create_child_object("ACE REAL TIME SOLAR WIND", "https://www.swpc.noaa.gov/products/ace-real-time-solar-wind", True, \
                            purpose="Solar wind's high energy plasma",file_type="graphs",\
                            memo="ACEのリアルタイムの太陽風観測結果。右側にあるリストから、色々な観測機器のグラフが選べる。\
                             <br> EPAM(2桁keVから1桁MeVぐらいのプラズマ観測機器)とSIS(2桁MeVのプラズマの観測機器)のデータが特に大事。\
                             <br> (DSCOVRのほうがACEより新しいが、DSCOVRは高エネルギープラズマの観測機器が上手く行っていない。そのため、太陽風の高エネルギープラズマに関してはACEのデータを見る必要がある。)\
                             <br> EPAMは太陽風がなんらかの変化を示した時に、CMEかコロナホールによる高速太陽風かどちらが到来したのかを区別する手がかりとなる。\
                             <br> \
                             <br> 一般に\
                             <br> CMEではEPAMの示す値は急激に上がる。\
                             <br> 高速太陽風ではEPAMの示す値は徐々に上がっていく傾向にある。\
                             <br> \
                             <br> しかし、実際にはCMEと高速太陽風が同時に到来するなど、一筋縄ではいかないケースも多い。\
                             <br> そのためCMEと高速太陽風のどちらが到来しているかについての判断を行う際は、ソース(=太陽表面における現象)との突き合わせも重要である。\
                             <br> 発生源がはっきりしない場合、高速太陽風やCMEが到来しているかは保留にせざるを得ないことも多い。\
                             <br> \
                             <br> 2桁keVから1桁MeVぐらいのプラズマがCMEによって運ばれてきているとき、(高速太陽風によって運ばれている時ではない。)以下のようなことが言える。\
                             <br> &nbsp&nbsp;EPAMで観測できるプラズマ、すなわち比較的エネルギーの低いプラズマはCMEの先端にトラップされているだけであり、CMEを抜け出して先行することは少ない。\
                             <br> &nbsp&nbsp;そのため、EPAMが上がり始めるときはCMEはもう近くまで来ている事が多い。\
                             <br> &nbsp&nbsp;SISで観測できる2桁MeVのプラズマは、CMEよりだいぶ先行していることもあるが、それはかなり大きいCMEの場合のみ見えることが多い。")
        },

        "STEREO Solar wind": create_child_object("STEREO Solar wind", "https://www.swpc.noaa.gov/products/solar-terrestrial-relations-observatory-stereo", True, \
                                                purpose="Solar wind from different point", file_type="graphs",\
                                                memo="STEREO衛星による太陽風の観測データ。CME到来に関して複数点からチェックしたいときに見ると良いかも。\
                                                <br>STEREO衛星の位置は例えばReference_URLなど",
                                                refURL="https://iswa.gsfc.nasa.gov/IswaSystemWebApp/index.jsp?i_1=261&l_1=218&t_1=355&w_1=645&h_1=436.969&s_1=0_0_10_3&i_2=267&l_2=876&t_2=354&w_2=650.969&h_2=435.969&s_2=0_0_10_3"),

        "CME in space": { **create_child_object("SOHO LASCO C2 & C3", "https://soho.nascom.nasa.gov/data/Theater/", True, \
                        purpose="Confirmation of CME flying", file_type="images",\
                        memo="SOHOのコロナグラフを用いた観測機器LASCOによる動画。これにより、CMEがどのように宇宙空間に広がっていったかがわかる。 \
                         <br> SDOなどの太陽表面画像では太陽表面の事象しか見れないので、LASCOのデータを見るのは重要。\
                         <br> \
                         <br> CMEは一般に発生場所から等方的に広がる。そのため太陽面のうち地球から見えるどこかでCMEが発生している場合は、地球に到来する可能性がある。\
                         <br> 一方地球から見て裏側でCMEが発生している場合、到来の可能性はあまりない。\
                         <br> \
                         <br> LASCOの画像だけでは、CMEが太陽の地球側と反対側のどちらで発生しているか判断するのは困難である。\
                         <br> よって、SDOなどの太陽表面画像と付き合わせてCMEの発生源を特定するのが極めて重要である。\
                         <br> なおCMEの発生において、SDO等で確認できる太陽表面での変動現象から、LASCOでプラズマの放出が確認できるまで1時間程度の遅延が生じる事が多い。\
                         <br> これは、太陽表面からLASCOの画角に収まるまでの距離をCMEが伝搬するのにかかる時間によるものである。\
                         <br> \
                         <br> またLASCOで見て中央から360度プラズマが広がっているように見える場合、これをフルハローCMEと呼ぶ。\
                         <br> フルハローCMEはCMEが地球直撃コースである可能性が極めて高いことを意味する。\
                         <br> \
                         <br> サイトにアクセスした後、C2かC3を選び日程を設定してGenerate。C2とC3の違いは視野のみ。\
                         <br> 画像の詳しい説明はReference_URL,\
                         <br> LASCOの仕様に関する論文はreference_URL2に記載。",
                          refURL="https://soho.nascom.nasa.gov/data/realtime/image-description.html",
                          refURL2="https://link.springer.com/article/10.1007/BF00733434"),

                          **create_child_object("SOHO LASCO C2 & C3 Diff and mesurement", "https://cdaw.gsfc.nasa.gov/movie/make_javamovie.php?&img1=lasc2rdf&img2=lasc3rdf", True, \
                        purpose="Confirmation of CME flying", file_type="images",\
                        memo="LASCOの動画でCMEを確認しようとした際、淡くてわかりにくいことがある。そこで、前の画像との差を表示する差分版を使うと見やすくなる。\
                             <br> リンクのサイトは、CDAW Data CenterがSOHOのLASCOデータの差分版を見やすく表示しているものである。\
                             <br> \
                             <br> このサイトはCMEの速度の簡易的な計算を補助する機能もある。画像の下のmesurementというリンクを押すと計測用のページに飛べる。\
                             <br> 計測用のページでは、動画のどこかを選択すると、その点の位置と、押した時刻が表示される。\
                             <br> これを用いるとCMEの大まかな速度を計算しやすくなる。\
                             <br> 距離が分かりづらいが、H(Rs)が中心からの距離(単位Rsは太陽半径)である。\
                             <br> \
                             <br> 過去のデータが見たい場合、下のPrev DayやNext Day使うことができる。\
                             <br> 数十日以上遡りたい場合、\
                             <br> https://cdaw.gsfc.nasa.gov/movie/make_javamovie.php?img1=lasc2rdf&img2=lasc3rdf&date=20240127\
                             <br> のように、URLの後ろに&date=YYYYMMDD を入れると見ることができる。\
                             <br> \
                             <br> CDAWによる差分表示サイトは、主にC3が上手く表示されないことがある。(サイトの問題ではなく、データ欠損のこともある)\
                             <br> その場合、公式を参照すると良い。Reference_URL2を参照。サイトの下にあるLASCO C2 COMBOや、C3 COMBOがそれ。\
                             <br> アーカイブはReferrence_URLのDailyという名前がついたページから見れるが、よくサーバーダウンしてる気がする。\
                             <br> Dailyから見るアーカイブは現在の月より前のものしか見れないので注意。",\
                                refURL="https://cdaw.gsfc.nasa.gov/index.html",\
                                refURL2="https://soho.nascom.nasa.gov/data/realtime/mpeg/"),
                        **create_child_object("CACTUS Auto-CME-catalog", "https://www.sidc.be/cactus/", True, \
                        purpose="Confirmation of CME flying", file_type="graphs",\
                        memo="ESAによる、LASCOのデータを持ちいたCMEのカタログ。CMEを自動で検出し、速度分布などを計算しグラフにして掲載している。\
                                <br> フルハローか否かや、速度の分布を表示しているのが便利。CMEの性質の簡易的な確認に使える。自動検出及び計算であることに注意。\
                                <br> Latest CME detectionsをクリックすると最近のイベント一覧に飛べる。その中で興味のあるページを見れば良い。なお、refURLにもLatest CME detectionsのページURLを記載してある。\
                                ", refURL="https://www.sidc.be/cactus/out/latestCMEs.html"),

                        **create_child_object("STEREO Coronagraph", "https://stereo.gsfc.nasa.gov/beacon/", True, \
                                              purpose="Confirmation of CME flying", file_type="images",\
                                                memo="STEREO衛星によるコロナグラフ画像。使い勝手はLASCOと比べるとあまり良くない。\
                                                    <br> SOHOと違う視点からのコロナグラフが見たい際に使えるはずだが、2023年頃はSTEREOはSOHOと同じ場所を飛んでいる。そのため、LASCOが不調な場合や見づらい場合の代替としてがメインになりそう。\
                                                    <br> リンク先サイトの画像一覧の中からSTEREO Aheadと書いてあるコロナグラフの画像を見つけることができる。説明がついていない数字だけのリンクを押すと画像をダウンロードすることができる。\
                                                    <br> (Aheadは衛星の名前なので、特に特別な意味はない。《もともとStereoはAheadとBehindの2機構成だった。Behindは壊れた。》)\
                                                    <br> MPEGと書いてあるやつからは、MPEG形式の動画をダウンロードできる。なお、Mp4のことではない。MPEGを再生するのは意外とめんどくさい可能性。Windows11の場合、Microsoft clip champが、デフォルトでついてる機能の中で一番MPEGを見やすい気がする。\
                                                    <br> リンク先サイトは数日前のものしか見れないため、過去のものを見たい場合はReference_URLから。\
                                                    ", refURL="https://stereo.gsfc.nasa.gov/cgi-bin/images")
                         
        },

        "Solar Wind Simulation": {
                    **create_child_object("SUSANOO", "https://cidas.isee.nagoya-u.ac.jp/susanoo/", True, \
                    purpose="Refer for forecast", file_type="graphs",\
                    memo="太陽風シミュレーションモデルSUSANOOによるL1地点での太陽風予報および、太陽系空間での太陽風予報。 <br> MHDシミュレーションらしい。 \
                    <br> 磁場のグラフの、白色は全磁場、赤色は南北成分っぽい。 <br> nictのサイトのほうが見やすいかもしれない。(Reference_URL参照)",\
                    refURL="https://origin-swc.nict.go.jp/forecast/magnetosphere.html"),

                    **create_child_object("WSA-ENLIL-CONE Nowcast and Forecasts", "https://iswa.gsfc.nasa.gov/IswaSystemWebApp/", True, 
                                            purpose="Refer for forecast", file_type="graphs",\
                                            memo="WSA_Enlil-CONEモデルによるシミュレーション。CONEモデルを用いることにより、HaloCMEの角度とかをちゃんと推定しているっぽい? WSA-ENLIL使うよりこっちのほうが良さそうかも\
                                            <br>リンク先自体はISWAのアプリサイト。ここでは好きな画像やグラフを好きな位置にレイアウトすることができる。\
                                            <br>WSA-ENLIL-CONEの結果は、左上のBrowse/WSA-ENLIL Cone Model CME Evolution for Eventsと、Browse/SA-ENLIL Cone Model Timelines for Eventsから見ることができる。\
                                            <br>各ウィンドウを出したあとは、左上のDensityとかVelocityなどを選ぶと、ウィンドウの内容を変更できる。\
                                            <br>各ウィンドウ、左下からauto update modeとtime range modeを切り替えることができる。)\
                                            <br>なお、レイアウトはjson形式で保存できる。\
                                            <br>\
                                            <br>WSA-ENLIL-CONEを確認するうえでのおすすめのレイアウトjsonをReference_URLに記載してある。\
                                            <br>ダウンロードした上で、ISWAのサイトにある上のメニューのLoad Layoutから読み込むことができる。\
                                            <br>(手順1. 本サイトのReference_URLにあるISWALayout.jsonを右クリックして、名前をつけてリンク先を保存、でダウンロード。)\
                                            <br>(手順2. ISWAのアプリサイトの上のメニューにあるLoad Layoutを選択、先程ダウンロードしたファイルを読み込む。)\
                                            <br>\
                                            <br>シミュレーション開始時の日付?によって大きく結果が変化することあり。\
                                            <br>WSA、ENLIL、CONEの3つのモデルについての詳細はrefURL2など参照。",
                                            refURL= '<a href="ISWALayout.json">ISWALayout.json</a>' ,refURL2="https://www.diva-portal.org/smash/get/diva2:1778148/FULLTEXT01.pdf"),
                                        
                    **create_child_object("WSA-ENLIL SOLAR WIND PREDICTION", "https://www.swpc.noaa.gov/products/wsa-enlil-solar-wind-prediction", True, \
                    purpose="Refer for forecast", file_type="graphs",\
                    memo="太陽風シミュレーションモデルWSA-EnlilによるL1地点及びSTEREO衛星での太陽風予報および、太陽系空間での太陽風予報。 <br> SUSANOOと異なり、太陽風の磁場情報が入っていない。そのため、シミュレーション結果にも速度と密度しかなく磁場予測がないが、見やすい。")
        },
    },
    
    "Solar Radio Burst": {

        "Global ground observation of bursts": create_child_object("e-callisto", "http://soleil.i4ds.ch/solarradio/callistoQuicklooks/", True, \
                                          purpose="Confirmation of solar radio burst", file_type="images",\
                                            memo="太陽電波バーストの観測データ。世界各地（地表）で観測された、様々な周波数帯での観測結果が見れる。<br> \
                                            太陽活動に伴って様々な型のバーストが発生していることを確認することができる。特に太陽フレアやCMEについて検討する際の指標になる。<br> \
                                            日付を指定して、見たい観測点と時間帯のデータのImageとある文字にマウスカーソルを重ねると、スペクトルデータが表示される。<br>\
                                            Imageをクリックすると拡大画像が表示される。Fitsをクリックするとzipファイルがダウンロードされる。<br>\
                                            Reference_URLより、各観測点と、その観測点で観測できる周波数帯のデータが確認できる。<br>\
                                            Reference_URL2には、e-callistoのトップページを記載。<br>\
                                            各月のバースト検出数の総計が見たい場合は、<br>\
                                            https://www.e-callisto.org/Data/BurstCountsYYYYMM.png のYYYYMMを編集してアクセスすると良い。",
                                            refURL="https://soleil.i4ds.ch/solarradio/data/readme.txt", refURL2="https://www.e-callisto.org/"),
        

    },

    
    "Geomagnetic disturbances": {

        "Near real time Geomagnetic data": create_child_object("地磁気世界資料センター京都 地磁気速報値", "https://wdc.kugi.kyoto-u.ac.jp/plot_realtime/quick/index-j.html", True, \
                                                               purpose="Confirmation of geomagnetic disturbances", file_type="graphs",\
                                                                memo="世界各所の地磁気データの速報値が見れる。結構早い＋使いやすいので、今世界のどの場所でどれぐらい地磁気が乱れているか見るのに良い。\
                                                                    <br> 「今日」を押すことで今の状態を表示できる。データ内容に関しては、Reference_URLから色々確認できる。(Geomagnetic dataのrefURLのReal-time(Quicklook)Geomagnetic dataから、リアルタイムデータに飛べる。)\
                                                                    <br> 場所の記号に関しては、Reference_URL2の27P、Station List by Abbreviation (ABB) Codeに記載されている。",\
                                                                        refURL="https://wdc.kugi.kyoto-u.ac.jp/wdc/Sec3.html",\
                                                                        refURL2="https://wdc.kugi.kyoto-u.ac.jp//wdc/pdf/Catalogue/Catalogue.pdf"),

        "Kp index": create_child_object("SWPC PLANETARY K-INDEX", "https://www.swpc.noaa.gov/products/planetary-k-index", True,\
                    purpose="Magnitude of geomagnetic disturbances across the globe",file_type="graphs",exampleVal="最大Kp指数:2.67(一日のうち最も大きいKp)  日合計値:13.66(3時間ごとに区切って出されるKpを、その日のもの全て(8つ)足す)  NOAA Scale: G0",\
                    memo="地球全体での地磁気擾乱の大きさを示す、Kp指数が見れる。(Kp index = Planetary K-index) \
                        <br> Kp指数は、地磁気擾乱の大きさを示すものとして最もメジャー\
                        <br> また、Kp指数をもとにした磁気擾乱に関するNOAAスケールもこのページに載っている。<br>スケールの説明はReference_URLのGeomagnetic Stormsタブに載っている。",\
                        refURL="https://www.swpc.noaa.gov/noaa-scales-explanation"),

        "K index": create_child_object("KAKIOKA K-INDEX", "https://origin-swc.nict.go.jp/trend/geomag.html",True,\
                    purpose="Magnitude of geomagnetic disturbance at Kakioka",file_type="graphs",exampleVal="最大K指数:3(一日のうち最も大きいK)  日合計値:13(3時間ごとに区切って出されるKを、その日のもの全て(8つ)足す)  地磁気活動度: 静穏",\
                    memo="ローカルでの地磁気擾乱の大きさを示すK指数のうち、柿岡のものが見れる。日本での地磁気擾乱を考える際に重要。H componentは水平分力、D componentは偏角を表す。 \
                        地磁気活動度(Quiet, Active...)も載っている。地磁気活動度の基準はReference_URL参照。 <br> なおこの基準はNICTによるもので、K指数の最大値を元にしたものである。(ISESの基準に合わせているようだが、ISES側での定義がどこで公表されているかは不明)\
                        <br> 日合計値や各componentの詳細はReference_URL2参照。リンク先に日最大値を元に定められている地磁気活動度の基準がある。これは気象庁が設定したものであり、NICTによるものとは別であることに注意。 <br> 一般に、NICTによるものが参照されていることが多いらしい。", \
                        refURL="https://origin-swc.nict.go.jp/knowledge/criteria_icon.html",\
                        refURL2="https://www.kakioka-jma.go.jp/knowledge/glossary.html"),


        "Dst index": create_child_object("DST-INDEX", "https://wdc.kugi.kyoto-u.ac.jp/dstdir/index-j.html",True,\
                    purpose="DST-index",file_type="graphs",\
                    memo="DST指数。磁気嵐の判定などに。予報ではそんなに使わないのかも?"),

        "AE index": create_child_object("AE-INDEX", "https://wdc.kugi.kyoto-u.ac.jp/aedir/index-j.html",True,\
                    purpose="AE-index",file_type="graphs",exampleVal="None",\
                    memo="AE指数。サブストームの判定などに。予報ではそんなに使わないのかも?"),
        
        "GOES MAGNETOMETER": create_child_object("GOES MAGNETOMETER", "https://www.swpc.noaa.gov/products/goes-magnetometer",True,\
                    purpose="Magnetic field at L1",file_type="graphs",exampleVal="None",\
                    memo="GOES衛星の観測した、静止軌道での磁場の変動を示す。急激な変化により、太陽風による磁気圏の急激な圧縮を読み取ることができる。\
                        <br> GOES衛星は静止軌道にいるために一日で昼側と夜側と通過する。これに伴う定期的な磁場の変動があることに注意。"),

        "Geomagnetic storm overview": create_child_object("磁気嵐 月別概況", "https://www.kakioka-jma.go.jp/obsdata/mstorm/mstorm_index.php",True,\
                                                          purpose="Geomagnetic storm overview",file_type="texts",exampleVal="None",\
                                                            memo="柿岡/女満別/鹿屋観測所による、磁気嵐の月別概況。磁気嵐の発生状況を月別にまとめている。\
                                                                <br> 1990年から見ることができ、かなり視認性が良い。→ここ数十年の間の磁気嵐をサーチする際に最適。\
                                                                    <br> Reference_URLには、英語版を記載してある。"\
                                                                        ,refURL="https://www.kakioka-jma.go.jp/en/obsdata/mstorm/mstorm_index_en.php"),

    },

    "Radiation belts": {
        "GOES Electron 24-h fluences and flux": {**create_child_object("NICT GOES Electron Fluences and flux","https://origin-swc.nict.go.jp/trend/electron.html",True,\
                        purpose="Checking the electron 24-h fluences and flux in the radiation belt", file_type="graphs",\
                        memo="GOESが取得した2MeV以上の電子fluxとfluencesが確認できる。fluencesとは、fluxを24時間で積分した値。GOESデータを元にNICTが積分した結果を出している。\
                            <br> 静止軌道衛星の観測データ24時間の総和なので、地球一周分の総和を取っている。すなわち、地球を囲う放射線帯全体の状況を表していると言える。\
                            <br> 放射線帯予報では、fluxよりもfluencesが重視されることがある。\
                            <br> 放射線帯全体の状況を表せることが主な理由。(Localな経度の情報を把握し発信することに重点を置かないケースがある)"),
                        
                        **create_child_object("NOAA GOES Electron Flux","https://www.swpc.noaa.gov/products/goes-electron-flux",True,\
                            purpose="Checking the electron flux in the radiation belt", file_type="graphs",\
                            memo="GOESが取得した2MeV以上の電子fluxの時間変化。7daysで見るのが良さそう。\
                                <br> 現在の「GOESがいる経度」の放射線帯の電子fluxがわかる。グラフのNとMはNoonとMidnightの略で、衛星が昼側、夜側にいることを指す。\
                                <br> なお、GOES-16は西経75.2度、GOES-18は西経136.9度の静止衛星。 <br> 静止軌道は、平均的な放射線帯外帯の外端にあたる。"),
                        
        },

        "Himawari Electron 24-h fluences and flux": create_child_object("HIMAWARI SEDA DATA VIEWER","https://himawari-seda.nict.go.jp/dataplot",True,\
                            purpose="Checking the electron flux in the radiation belt", file_type="graphs",\
                            memo="ひまわりが取得したMeV帯の電子fluxの時間変化や24時間電子fluencesが見れる。\
                                <br> fluxについては、現在の「ひまわりがいる経度」の放射線帯の電子fluxがわかる。横軸はUTなので注意。\
                                <br> fluencesとはfluxを24時間で積分した値。ひまわりデータを元にNICTが積分した結果を出している。\
                                 <br> 静止軌道衛星の観測データ24時間の総和なので、地球一周分の総和を取っている。すなわち、地球を囲う放射線帯全体の状況を表していると言える。\
                                <br> 放射線帯予報では、放射線帯全体の状況を表せることからfluxよりもfluencesが重視されることがある。\
                                <br> サイトの上の方にある、設定を色々いじったあと右上のPlotというボタンを押すとグラフが更新される。ひまわり8号、9号のデータが共に見れる。\
                                <br> ひまわりの経度は、8号9号ともにおよそ140.7度(0.05度離れているらしい。)。\
                                <br> 静止軌道は、平均的な放射線帯外帯の外端にあたる。"),

        "Electron fluences forecast": {**create_child_object("電子フルエンス予報","https://radi.nict.go.jp/",True,\
                                        purpose="Reference for forecast electron fluences", file_type="text", \
                                        memo="NICTによる放射線帯における24時間 Electron fluencesの、今後24時間、明日、明後日の予報。シミュレーションや統計モデルなど、複数のをもとに行われている。\
                                                <br> 予報の参考になる。静穏等々の基準についてはReference_URL参照。",\
                                                    refURL="https://radi.nict.go.jp/about/#level"),
                                        
                                        **create_child_object("RELATIVISTIC ELECTRON FORECAST MODEL", "https://www.swpc.noaa.gov/products/relativistic-electron-forecast-model",True,\
                                                            purpose="Reference for forecast electron fluences", file_type="graphs",\
                                                            memo="NOAAによる放射線帯における24時間 Electron fluencesの、今後24時間、明日、明後日の予報。\
                                                            2MeV以上の電子の24時間フルエンスの予報になっている。"),
            },
        
        
        "Electron flux forecast": create_child_object("静止軌道危険度予測","https://radi.nict.go.jp/satellite/",True,\
                purpose="Reference for forecast electron flux", file_type="graphs",\
                memo="シミュレーションや統計モデルによる電子fluxの時間変化の予測。 <br> ひまわり8号、GOES衛星それぞれの軌道における電子fluxの大きさの予報値が示されている。"),
    },

    "Ionosphere": {

        "Ionosonde": {
            **create_child_object("foF2 and GEONET TEC time change at Japan","https://swc.nict.go.jp/trend/ionosphere.html",True,\
                                  purpose="Checking ionospheric positive and negative storm", file_type="graphs",\
                                    memo="F層付近での電子密度(foF2)、上空の全電子密度(GEONET TEC)の変化を表す。 <br> どちらのデータも正相電離圏嵐、負相電離圏嵐の確認に使える。\
                                         <br>  2時間以上Ip2以上やIn2以上に入っている場合は電離圏嵐とみなす(Ip、InはIスケール)。Iスケールが0と1は静穏。\
                                         <br> なお電離圏嵐が発生した際は、fOF2、TECともにグラフ上に電離圏嵐が発生した旨が表示される。\
                                         <br> Iスケールの意味合いはReference_URL参照。\
                                         <br> 電離圏嵐の判定に関して言えばfoF2、GEONET TEC2つの違いはあまり注意しなくてよく、クロスチェックの意味合いが強い。",
                                         refURL="https://swc.nict.go.jp/knowledge/i-scale.html"),

            **create_child_object("GEONET TEC map","https://aer-nc-web.nict.go.jp/GPS/QR_GEONET/",True,\
                                  purpose="Checking ionoshpheric storm",file_type="images",
                                  memo="日本上空の電子密度の空間分布を示したもの。ここでいう電子密度とは、上空までの全電子密度。\
                                       <br> 日本のどの領域で電離圏嵐が発達しているかがわかる。"),

            **create_child_object("Observed foEs","https://swc.nict.go.jp/trend/es.html",True,\
                                                purpose="Checking Sporadic E layer", file_type="graphs",\
                                                memo=" スポラティックE層の発生の時間プロットを見る際に使える。(スポラティックE層の発生だけみたいのであればイオノグラムの方が良い。)\
                                                 <br> 8MHzを超えた時間はスポラティックE層が発生していた可能性がある。\
                                                 <br> 詳細やアーカイブは、Reference_URLの「電離圏パラメータプロット」を参照。",\
                                                    refURL="https://wdc.nict.go.jp/IONO/HP2009/ISDJ/index.html"),
        },

        "Ionogram": { 
                             **create_child_object("NICT Site Ionogram Viewer","https://swc.nict.go.jp/forecast/ionosphere.html",True,\
                                                purpose="Checking Sporadic E layer", file_type="graphs",\
                                                memo="ページを少しスクロールして出てくる、「国内イオノゾンデ定常観測」の場所を参照。\
                                                     <br> ぱっと現況確認したいときはこれが見やすい。なお、色はエコー強度を意味する。\
                                                     <br> スポラティックE層とデリンジャー現象の発生を確認したい場合は、これを使うと良い。\
                                                     <br>\
                                                     <br> スポラティックE層: 高度100km前後(E層)にて8MHz以上でエコーがあれば、スポラティックE層とみなしても良い。\
                                                     <br> &nbsp&nbsp&nbsp&nbsp;縦軸で100km前後のところかつ横軸が8MHz以上の場所にエコーがあるかを確認する。\
                                                     <br> デリンジャー現象: D層が電波を吸収した結果、E層(高度100km前後)より上のエコーが消えるのがデリンジャー現象。\
                                                     <br> &nbsp&nbsp&nbsp&nbsp;強いデリンジャー現象の時は、イオノグラムがブラックアウト(一面真っ黒)する。一切のエコーが帰ってこない。\
                                                     <br> &nbsp&nbsp&nbsp&nbsp;ある程度の規模のデリンジャー現象では、高度100kmの前後のエコーが消える。"),

                              **create_child_object("Color Ionogram Viewer details","https://wdc.nict.go.jp/ionog/js_viewer/js_01.html",True,\
                                                purpose="Checking Sporadic E layer", file_type="graphs",\
                                                memo="イオノグラムのカラープロットの詳細版。過去のデータなども見れる。左側で設定してDisplayを押すと描画される。\
                                                      <br> 操作方法はReference_URLを参照。\
                                                      <br> 詳細はReference_URL2を参照。",\
                                                    refURL="https://wdc.nict.go.jp/IONO/HP2009/ISDJ/exp-ionogram_viewer_color.html",\
                                                    refURL2="https://wdc.nict.go.jp/IONO/HP2009/ISDJ/index.html")

        },

        "GOES Dellinger effect": create_child_object("Dellinger phenomenon", "https://swc.nict.go.jp/trend/dellinger.html", True,\
                                purpose="Checking Dellinger effect", file_type="graphs",\
                                memo="デリンジャー現象の世界的な現況マップ。 <br> ローカルなデリンジャー現象の把握にはイオノグラムを用いたほうが良いため、あまり使わないかもしれない。\
                                    <br>詳細やアーカイブは、Reference_URLを参照。",\
                                refURL="https://wdc.nict.go.jp/x-ray/index.html"),
        
        "CTIPE TOTAL ELECTRON CONTENT FORECAST": create_child_object("CTIPE TOTAL ELECTRON CONTENT FORECAST", "https://www.swpc.noaa.gov/products/ctipe-total-electron-content-forecast", True,\
                                purpose="Checking Total Electron Content", file_type="graphs",\
                                    memo="CTIPEモデルによる、全電子密度(垂直に足し合わせた密度、TEC)の現況。Forecastとあるがモデルを用いた現況の意味合いが強そう。\
                                        <br> 全世界のマップが見れるのが一応特徴ではある。ただ、TECに関係するイベントはローカルで見たほうが良いため、あまり使わないかもしれない。"),
        "D-Region Absorption Prediction": create_child_object("D-Region Absorption Prediction", "https://www.swpc.noaa.gov/products/d-region-absorption-predictions-d-rap", True,\
                                purpose="Checking D-Region Absorption Prediction", file_type="Images",\
                                    memo="D層吸収の予想。D層吸収は、太陽フレアやCMEによるX線、紫外線の増加により、D層が電波を吸収する現象。\
                                    極冠吸収やデリンジャーの際に確認すると良いかも。X線や高エネルギープロトンによって発生。"),
        

    },

    "Aurora": {

        "AuroraMax Live Feed": create_child_object("AuroraMax Live Feed", "https://auroramax.com/live", True,\
                                purpose="Checking Aurora", file_type="images",\
                                memo="カナダ、イエローナイフにおけるオーロラのライブカメラ。オーロラが発生しているか確認するときに使える。"),

        "昭和基地カメラ": create_child_object("昭和基地カメラ", "https://polaris.nipr.ac.jp/~acaurora/syoCDC/index.html", True,\
                                       purpose="Checking Aurora", file_type="images",\
                                        memo="昭和基地におけるオーロラのライブカメラ。オーロラが発生しているか確認するときに使える。\
                                            <br>右上のAnimationを選ぶことで、過去ログやこの数日の動きを見ることができる。"),
                                

        "NOAA OVATION model Aurora forecast": create_child_object("AURORA - 30 MINUTE FORECAST", "https://www.swpc.noaa.gov/products/aurora-30-minute-forecast", True,\
                                purpose="Checking Aurora forecast", file_type="graphs",\
                                memo="オーロラ予報。30-90分後のオーロラ予報を提供する。\
                                    <br> OVATION modelというモデルを使っている。L1での観測データと高エネルギープラズマの振りこみの関係から求めている模様。"),

        "NICT Aurora forecast": create_child_object("NICT Aurora forecast", "https://aurora-alert.nict.go.jp/", True,\
                                                    purpose="Checking Aurora forecast", file_type="graphs",\
                                                        memo="NICTのオーロラ予報。使い所がわからんけど一応..."),

    },

    "Information sites": {
        "NICT Space weather forecast Guide": create_child_object("宇宙天気予報ユーザーガイド","https://swc.nict.go.jp/knowledge/", True,\
                                                                 memo="NICTの宇宙天気のユーザーガイド。指標などの参考に。"),

        "NICT space weather forecast Trend": create_child_object("NICT Space Weather Forecast Trend Site","https://origin-swc.nict.go.jp/trend/",True,\
                                                           memo="各領域、各現象をクリックしたら関連グラフや数値と元データのリンクがすぐに出てくる。"),

    },

    "Link collection site": {


        "NICT space weather forecast Link collection": create_child_object("NICT Space Weather Forecast Links","https://origin-swc.nict.go.jp/link/",True,\
                                                           memo="NICTの宇宙天気予報のサイトのリンク集。色々なサイトとか載ってる。"),

        "SOHO space weathers": create_child_object("SOHO Space Weather", "https://soho.nascom.nasa.gov/spaceweather/",True,\
                                                   memo="SOHOのサイトにあるリンク集。オーロラ予報とかシミュレーション予報とか載ってるの嬉しさがある。"),

        "ISWA" :create_child_object("ISWA Web App","https://iswa.gsfc.nasa.gov/IswaSystemWebApp/",True,\
                                    memo="NASAのISWAのWebアプリ。色々なデータが見れる。なんかたまにサーバーが落ちてたりする気がする。\
                                        <br> かなり多くのシミュレーションデータや観測データをカバーしている。\
                                        <br> 詳細はReference_URLを参照。",refURL="https://ccmc.gsfc.nasa.gov/tools/iSWA/"),

        "宇宙天気ニュース" :create_child_object("宇宙天気ニュース","https://swnews.jp/",True,\
                                    memo="宇宙天気ニュースのサイト。宇宙天気に関するニュースやリンクサイトが日本語でまとめて掲載されている。\
                                        <br> 鹿児島工業高等専門学校の篠原 学先生により運営されている模様。"),
    }
}

# Save to a JSON file
with open("./Datas/space_weather_info.json", "w") as f:
    json.dump(space_weather_info, f, indent=4, ensure_ascii=False)

"/mnt/data/space_weather_info.json"
