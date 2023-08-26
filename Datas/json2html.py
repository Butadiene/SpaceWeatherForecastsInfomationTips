import json

def get_value_from_key(d, target_key):
    """
    Recursively search for a key in a dictionary and return its value.
    
    :param d: Dictionary to search
    :param target_key: Key to search for
    :return: Value associated with the key or None if not found
    """
    if target_key in d:
        return d[target_key]
    
    for key, value in d.items():
        if isinstance(value, dict):
            result = get_value_from_key(value, target_key)
            if result is not None:
                return result
    return None


def json_to_html(data, depth=0):
    html = ''
    spacing = '  ' * depth

    # Determine font size based on depth
    font_size = 20

    # If the data is a dictionary, convert each key-value pair to HTML
    if isinstance(data, dict):

        html += f'<div style="margin-left:20px; font-size:{font_size-depth*1.5}px;">'
        for key, value in data.items():
            if isinstance(value, (dict, list)):
                if depth > 0:  # Only make the topmost object collapsible
                    html += f'{spacing}<div class="collapsible"  style="color: green;" onclick="toggleVisibility(this)"><strong>{key}</strong></div>'
                    html += f'<div class="content" style="display: none;">{json_to_html(value, depth+1)}</div>'
                else:
                    html += f'{spacing}<strong>{key}:</strong> {json_to_html(value, depth+1)}'
            else:
                if ("External_access" not in key):
                    if ("URL" in key and is_url(value)) or ("Reference_URL" in key and is_url(value)) or ("Reference_URL2" in key and is_url(value)):
                        value = f'<a href="{value}" target="_blank">{value}</a>'
                    html += f'{spacing}<strong>{key}:</strong> {value}<br>'
        html += '</div>'

    # If the data is a list, convert each item to HTML
    elif isinstance(data, list):
        html += '<ul>'
        for item in data:
            html += f'{spacing}<li>{json_to_html(item, depth+1)}</li>'
        html += '</ul>'

    return html

def is_url(s):
    """Check if a string is a URL."""
    return s.startswith(('http://', 'https://'))

def convert_json_file_to_list(filename):
    with open(filename, 'r') as f:
        data = json.load(f)
    html_data = json_to_html(data)
    return html_data

def get_site_info(data,target):
    return json_to_html({target: get_value_from_key(data,target)},depth=1)

def lists_only_space_weather_info(filename):
    with open(filename, 'r') as f:
        data = json.load(f)
    list_data = convert_json_file_to_list('./Datas/space_weather_info.json')

    head_data = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Space Weather Forecast Infomartion Sites Lists</title>
    </head>
    """
    body_data = "<body>"+\
    "<h1>Space Weather Forecast Infomartion Sites Lists</h1>"+\
    "<h2>Information Lists</h2>"+"ここに記載してある一切の情報について、作者は責任を負いません。"+\
    list_data+"</body></html>"
    
    
    script = '''
    <script>
    function toggleVisibility(element) {
        var content = element.nextElementSibling;
        if (content.style.display === "none") {
            content.style.display = "block";
        } else {
            content.style.display = "none";
        }
    }
    </script>
    '''
    html_data = head_data+body_data+script
    return html_data


def intro_space_weather(filename):
    with open(filename, 'r') as f:
        data = json.load(f)
    list_data = convert_json_file_to_list('./Datas/space_weather_info.json')

    head_data = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Space forecast tips</title>
    </head>
    """
    body_data = "<body>"+\
    "<h1>Space Weather Forecast Tips</h1>"+\
    "<h2>Information List</h2>"+\
    list_data+\
    f""" ここに記載してある一切の情報について、作者は責任を負いません。
    <h2> Forecast Process Template </h2>
    <p style="color: red;">Warning: 宇宙天気予報は様々なデータを俯瞰的に見て、多くの状況に応じて判断しなければならない。ここに載せるのは1テンプレートにすぎない。</p>

    <ol>
        <li>
            各国の予報状況
            <p>各国の予報状況を確認し、現在の太陽活動や地磁気活動がどの程度Activeかをぼんやり把握する。{get_site_info(data,"Present Space Weather Forecast from ISES")}</p>
        </li>
        <li>
            太陽活動
            <p>太陽風活動、地磁気活動等の根本的な要因である太陽活動の詳細を把握する。 <br> その後、太陽フレア、プロトンフラックスの予報を行う。</p>
            <ol>
                <li>
                    GOESのX線フラックスの確認
                    <p>GOESのX線フラックスの直近数日の変動を確認する。GOESのX線フラックスは太陽フレアの基準となっており、大まかな太陽の活動度を把握できる。 <br> フレアがあったかの確認、バックグラウンドの大きさと傾向（増加傾向か否かなど）の確認が重要。{get_site_info(data,"GOES X-ray Flux")}</p>
                </li>
                <li>
                    プロトンフラックスの確認
                    <p>GOESのプロトンフラックスについての、直近数日の変動を確認する。太陽活動の活動度を把握する助けになる。{get_site_info(data,"GOES Proton Flux")}</p>
                </li>
                <li>
                    黒点全体の活動度の確認
                    <p>個々の黒点について確認する前に、太陽の地球側の面に見えている黒点全体の傾向について確認する。以下の指標を確認すると良い</p>
                    <ol>
                        <li>
                            F10.7(波長10.7cmの電波)の電波強度
                            <p>以下参考。値だけでなく、増加傾向か減少傾向かも重要。{get_site_info(data,"DRAO")} </p>
                        </li>   
                        <li>
                            太陽光球面の見えている黒点の総面積
                            <p>以下の黒点データリストに載っている面積を全部足すことで計算できる。値だけでなく、増加傾向か減少傾向かも重要。{get_site_info(data,"SOLAR REGION SUMMARY")}</p>
                        </li>
                        <li>
                            太陽黒点相対数
                            <p>以下参考。値だけでなく、増加傾向か減少傾向かも重要。{get_site_info(data,"SILSO : Daily estimated sunspot number")}</p>
                        </li>
                        <li>
                            月間太陽黒点相対数
                            <p>以下参考。{get_site_info(data,"SILSO : Monthly relative sunspot number")}</p>
                        </li>                        
                    </ol>
                </li>
                <li>
                    太陽活動の概観を動画で確認
                    <p>4日前からの太陽活動の動画を、波長帯ごとにざっと確認する。SDO衛星の動画を見ると良い。ここ4日で活動的な領域の大雑把な把握を、エネルギー帯別に行う。\
                        <br> フレアっぽいもの(高エネルギー帯で見える爆発的な現象)、コロナホールっぽいもの(211で見える黒い穴)、CMEっぽいもの(コロナやフレアが吹き飛んだ形跡)、黒点の量や分布、各黒点の磁場構造を大雑把に把握する。{get_site_info(data,"SDO Images")} {get_site_info(data,"SDO Images Dashboard")}</p>
                </li>
                <li>
                    活動領域(≒黒点近辺)の詳細を確認
                    <p>太陽表面の活動的な領域について、細かく把握していく。</p>
                    <ol>
                        <li>
                            活動領域(≒黒点近辺)の現況についての詳細な確認
                            <p>太陽表面の活動的な領域の現況について、細かく把握する。</p>
                            <ol>
                                <li>
                                    黒点位置と番号の確認
                                    <p>太陽表面に出ている黒点とそれに振られている番号を確認する。{get_site_info(data,"SOHO Sunspots")}</p>
                                </li>
                                <li>
                                    東端から回り込んでくる活動領域の確認
                                    <p>SDO画像の094などを見て東端から回り込んできた、あるいは回り込んできそうな位置する、黒点や活動的な領域を確認する。 <br> 未採番のものがあった場合、それについて認識する。{get_site_info(data,"SDO Images")} {get_site_info(data,"SDO Images Dashboard")}</p>
                                </li>
                                <li>
                                    各活動領域のデータを確認
                                    <p>以下のリストを見て、各活動領域のタイプ分け、面積、黒点数などを確認。\
                                        <br>この時、前日から各活動領域はどのように変化したのか（面積は増えたか、磁場構造は変わったか）を確認するのが重要。\
                                         <br> 前日と比べてリストから消えた活動領域は、西端を越えて裏側に回り込んだのか、衰退したのかの判定をする必要があり。{get_site_info(data,"SOLAR REGION SUMMARY")}</p>
                                </li>
                                <li>
                                    イベントリストを確認
                                    <p>各活動領域がどのぐらいの規模、数のフレアを起こしたかを確認する。以下のリストを使用すると良い。{get_site_info(data,"LMSAL last event reports")} \
                                    <br> また、イベントリストの確認の際にX線フラックスを突き合わせても良い。{get_site_info(data,"GOES X-ray Flux")}</p>
                                </li>
                            </ol>
                        </li>
                        <li>
                            各活動領域でのフレア予報の確認
                            <p>各活動領域で今後フレアが発生するかどうかについて、モデルによる予測を確認する。Deep Flare NetのDeFN-Rが良い。{get_site_info(data,"Deep Flare Net")}</p>
                        </li>
                    </ol>
                </li>
                <li>
                    注目すべき活動領域について、より細かく詳細を確認。
                    <p>上で得た各活動領域の詳細から、活動的、あるいは活動的な可能性がある活動領域をリストアップし、それらについて以下の手順でさらなる詳細を把握していく。</p>
                    <ol>
                        <li>
                        磁場構造の詳細な把握
                        <p>リストアップした活動領域について磁場構造、フラックスの大きさ、シアなどを確認し、活動領域の活動度についてより踏み込んだ解釈を行う。\
                            <br> SOLAR REGION SUMMARYでβ型と書いてあった黒点が実際よく見たらδ型、ということもあったりする。そのため、これまで得た情報を鵜呑みにせず、もう一度活動領域を丁寧に評価する。{get_site_info(data, "SHARP Vector Magnetograms")} {get_site_info(data, "SHARP Data Viewer")}</p>
                        </li>
                        <li>
                        太陽活動の動画の見直し
                        <p>リストアップした各活動領域に着目しながら、太陽表面の動画を見直す。 <br> 特に、AIA094やAIA1600でチカチカ光る光(磁場の浮上を示唆)、活動領域付近のフレアなどをもう一度確認。\
                        <br> チカチカ光る光を確認する際は、それが磁場の浮上によるものかフレアによるものかに注意。フレアイベントリストと付き合わせると確認しやすい。{get_site_info(data,"SDO Images")} {get_site_info(data,"SDO Images Dashboard")}{get_site_info(data,"LMSAL last event reports")}</p>
                        </li>
                    </ol>
                </li>
                <li>
                    フレア予報を考える。
                    <p>これまで得た各活動領域の情報を考慮しながら、太陽フレアの予報を考える。 <br> Mクラス以上のフレアを起こす可能性がある活動領域が存在するか、を基準に考えると良い。ここで、Deep Flare NETも助けになる。{get_site_info(data,"Deep Flare Net")}</[]>
                </li>
                <li>
                    プロトン現象の予報を考える。これについても、Mクラスフレアの発生を目安に考えると良い。プロトンフラックスの現況は以下。{get_site_info(data,"GOES Proton Flux")}
                <p></p>
        </li>
            </ol>
        </li>
        <li>
            デリンジャー現象
            <ol>
                <li>
                    デリンジャー現象の予報を考える。
                    <p>デリンジャー現象の予報を考える。デリンジャー現象は太陽フレアに伴うX線等の到来によって発生する。 <br> そのため、デリンジャー現象は太陽フレアの活発さとほぼ同じように生じる。よって太陽フレアの予報をもとに考えれば良い。\
                    <br> デリンジャー現象の現状は以下から把握できるが、イオノグラムから確認するのが割とメジャー。{get_site_info(data,"NICT Site Ionogram Viewer")} {get_site_info(data,"Observed foEs")}{get_site_info(data,"Dellinger phenomenon")}</p>
                </li>
            </ol>
        </li>
        <li>
            太陽風活動
            <p>地磁気擾乱の予報の大前提となる、太陽風活動の把握を行う。</p>
            <ol>
                <li>
                    L1地点での太陽風の現況把握
                    <p>L1地点での太陽風の現況把握を行う。これにより地球近辺にどのような太陽風が到来しているかがわかる。 <br> 現在の値はもちろん、上昇傾向か否かなどのトレンドを把握するのも重要。{get_site_info(data,"SWPC REAL TIME SOLAR WIND")}</p>
                </li>
                <li>
                    L1地点での高エネルギープラズマの現況把握
                    <p>高エネルギープラズマの到来についても把握を行う。到来している太陽風の解釈の助けになるため、後に行うCMEやコロナホールの解析に役立つ可能性がある。{get_site_info(data,"ACE REAL TIME SOLAR WIND")}</p>
                </li>
                <li>
                    コロナホールと高速太陽風の把握
                    <p>コロナホールとそれにより飛来する高速太陽風についての把握を行う。</p>
                    <ol>
                        <li>
                            コロナホールの確認
                            <p>SDO衛星のAIA 211の画像などから、太陽表面に存在するコロナホールを確認する。 <br> 3-4日前までは確認し、コロナホールが子午線にいるときの時刻などをチェック。{get_site_info(data,"SDO Images")} </p>
                        </li>
                        
                        <li>
                            L1地点での太陽風変動が高速太陽風によるものかを判断。
                            <p> L1地点で高速太陽風が来ているかを判断する。以下を参考材料とする。\
                            <br> 太陽風の速度が高い時間帯が存在するか、存在する場合はその時刻（特に速度が上昇を開始した時刻）を確認。\
                            <br> ACEのEPAMのデータを確認。2桁keVから1桁MeVぐらいのプラズマの変動を確認し、高速太陽風が示すことが多い変動を行っているかを確認。\
                            <br> 高速太陽風が到来している可能性があると判断した場合、3-4日前のコロナホールの画像(SDOのAIA 211画像など)を確認し、高速太陽風のもととなるコロナホールを探す。\
                            <br> (ソースとなるコロナホールが見当たらない時、高速太陽風の到来判断は保留したほうが良いことがある。)
                            {get_site_info(data,"SWPC REAL TIME SOLAR WIND")}{get_site_info(data,"ACE REAL TIME SOLAR WIND")}{get_site_info(data,"SDO Images")}</p>
                        </li>
                        <li>
                            1太陽周期前の太陽風、コロナホールの確認
                            <p>1太陽周期前(27日前)のSDO衛星211の画像と、太陽風のデータを確認する。\
                             <br> 1太陽風周期前に現在と同じようなコロナホールが存在するか、太陽風の値は1太陽風周期前と同じような変化を示しているかを確認。\
                             <br> もし、似たようなコロナホールがあり、太陽風が同じような変化を示していた場合、今後太陽風の値は前周期と同じような変化をたどる可能性がある。{get_site_info(data,"SDO Images")}{get_site_info(data,"SWPC REAL TIME SOLAR WIND")}</p>
                        </li>
                        <li>
                            シミュレーションの確認
                            <p>数値シミュレーションにより、コロナホールからどのように地球に太陽風が飛んでくるか、の予測を確認する。参考程度ではある。{get_site_info(data,"SUSANOO")}</p>
                        </li>
                        <li>
                            高速太陽風とコロナホールに関する現況把握
                            <p> 以上の情報から、現況把握を行う。着目点は以下が代表的。\
                            <br> 現在高速太陽風は到来しているか、している場合はどのコロナホールからのものか。\
                            <br> 現在太陽に見えているコロナホールのうち、今後地球に影響を及ぼす可能性があるものはあるか。\
                            <br> 例えば低緯度子午線付近に大きなコロナホールがあった場合、現在太陽風に顕著な変動がなくても、数日後に高速太陽風が到来する可能性があると言える。</p>
                        </li>
                    </ol>
                </li>
                <li>
                    CMEの把握
                    <p>CMEが発生しているか、到来しているかの把握を行う。様々なデータから複合的に判断する必要がある。</p>
                    <ol>
                        <li>
                            SDO画像から、CME候補となる現象の確認
                            <p> SDO衛星の画像などから、CMEの候補となる現象を確認する。\
                                高エネルギー帯の波長で見えるコロナの吹き飛び(一瞬暗くなるように見えたりもする)、AIA 304で見えるフィラメントの吹き飛びが重要。\
                            <br> 太陽表面から来るCMEは、3日程度かけて地球に到来するため、3-4日前から現在までの太陽画像を確認するのが大事。{get_site_info(data,"SDO Images")} {get_site_info(data,"SDO Images Dashboard")}</p>
                        </li>
                        <li>
                            LASCO画像による、宇宙空間への放出を確認
                            <p>SOHO衛星のコロナグラフによる観測機器LASCOのデータを確認し、宇宙空間へのプラズマの放出を確認する。\
                              <br> 淡くて見づらいことも多いので、差分画像も活用すると良い。\
                              <br> また、フルハローCMEがあるかも確認。{get_site_info(data,"SOHO LASCO C2 & C3")}{get_site_info(data,"SOHO LASCO C2 & C3 Diff")}</p>
                        </li>
                        <li>
                            CMEのリストアップ
                            <p> LASCO画像でのプラズマの放出、SDO画像でのCMEの候補現象の突き合わせを行う。\
                            <br> 両方で時間的に一致しているイベントはCMEと言えることが多いため、一致しているイベントをリストアップし、CME候補リストとする。\
                            <br> (「時間的に一致」について：SDOでのイベントからLASCOでプラズマ放出が見えるまで、1時間ほど遅延があることが多いことに注意。)\
                            <br> CME候補リストにおいては、どの領域で発生したものか、いつ発生したものなのか、を特に重視する。\
                            <br> 特に、太陽面の「地球から見えている側」で発生しているものを把握する。これらは地球に飛来する可能性がある。\
                            <br> CMEは発生した場所から等方的に広がることが一般的である。\
                            <br> そのため、CMEの発生箇所が低緯度か高緯度か、リム寄りか子午線寄りかに関係なく、地球から見える面で発生していれば飛来する可能性があることに注意。\
                            <br> また、リストアップされたCMEに対応する太陽フレアイベントがあるかを確認する。\
                            <br> なお、CMEはフレアを伴う事が多いが伴わないこともあるため、CME候補に対応するフレアイベントがなくても問題はない。(現象のより詳細な把握のために行う。){get_site_info(data,"Solar and geophysical events")}</p>
                        </li>
                            CMEの速度計算
                            <p> 地球に到来する可能性のあるCMEについて、LASCO等コロナグラフのデータを用いて、CMEの速度を計算する。\
                            <br> 計算した速度で太陽-地球間の距離を割って、CMEの到達時間を推測する。{get_site_info(data,"SOHO LASCO C2 & C3")}{get_site_info(data,"SOHO LASCO C2 & C3 Diff")}</p>
                        </li>
                        <li>
                            太陽風観測データとCMEの対応の確認
                            <p>先程到達時間を予想したCMEのうち、すでに地球に到達済み、あるいはもうすぐ到達する見込みのCMEがあることがある。\
                            <br> この場合は、太陽風観測データと突き合わせ、すでに到達済みかを検討する。
                             {get_site_info(data,"SWPC REAL TIME SOLAR WIND")}{get_site_info(data,"ACE REAL TIME SOLAR WIND")}</p>
                        </li>
                        <li>
                            シミュレーションとの対応の確認
                            <p>数値シミュレーションにより、CMEの到来がの予測されているかを確認し、自分が把握したCMEのリストと比較する。{get_site_info(data,"SUSANOO")}</p>
                        </li>
                    </ol>
                </li>
            </ol>
        </li>
        <li>
        地磁気擾乱
        </li>
        <!-- ... -->
    </ol>


    """\
    +"</body></html>"


    script = '''
    <script>
    function toggleVisibility(element) {
        var content = element.nextElementSibling;
        if (content.style.display === "none") {
            content.style.display = "block";
        } else {
            content.style.display = "none";
        }
    }
    </script>
    '''
    html_data = head_data+body_data+script
    return html_data



# Example usage:
info_html_data = intro_space_weather('./Datas/space_weather_info.json')
with open('./docs_list_and_forecast/space_weather_info.html', 'w') as f:
    f.write(info_html_data)

lists_only_html_data = lists_only_space_weather_info('./Datas/space_weather_info.json')
with open('./docs_info_lists/space_weather_info_lists.html', 'w') as f:
    f.write(lists_only_html_data)
