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


def is_url(s):
    """Check if a string is a URL."""
    return isinstance(s, str) and s.startswith(('http://', 'https://'))


def json_to_html(data, depth=0):
    """
    Convert JSON (dict or list) to HTML string.
    Collapsible sections are used for nested dict/list, except for the topmost dict.
    """
    html = ""
    # depth に応じてフォントサイズを調整 (ただし小さくなりすぎないよう max を設定)
    font_size = max(12, 20 - depth * 1.5)

    if isinstance(data, dict):
        # 最上位にはクラス .json-container、それ以降には .json-subcontainer を付与
        container_class = "json-container" if depth == 0 else "json-subcontainer"
        html += f'<div class="{container_class}" style="font-size:{font_size}px;">'
        for key, value in data.items():
            if isinstance(value, (dict, list)):
                if depth > 0:  # depth>0 の場合は折りたたみ要素にする
                    html += (
                        f'<div class="collapsible" onclick="toggleVisibility(this)">'
                        f'{key}</div>'
                        f'<div class="content">'
                        f'{json_to_html(value, depth+1)}</div>'
                    )
                else:
                    # トップレベルは普通に表示
                    html += f'<strong>{key}:</strong> {json_to_html(value, depth+1)}'
            else:
                # "External_access" がキーに含まれるものは表示しない
                if "External_access" in key:
                    continue

                # 値が URL の場合はリンク化
                if ("URL" in key and is_url(value)) or \
                   ("Reference_URL" in key and is_url(value)) or \
                   ("Reference_URL2" in key and is_url(value)):
                    value = f'<a href="{value}" target="_blank">{value}</a>'

                html += f'<strong>{key}:</strong> {value}<br>'
        html += '</div>'

    elif isinstance(data, list):
        html += '<ul class="json-list">'
        for item in data:
            html += f'<li>{json_to_html(item, depth+1)}</li>'
        html += '</ul>'

    return html


def convert_json_file_to_list(filename):
    """
    Load JSON from file and convert it to HTML string with json_to_html.
    """
    with open(filename, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return json_to_html(data)


def get_site_info(data, target):
    """
    Return an HTML snippet for the given 'target' key within 'data', 
    wrapped in the same JSON-to-HTML style. Depth=1 for partial indentation.
    """
    found_data = get_value_from_key(data, target)
    if found_data is None:
        return f'<strong>{target}:</strong> (No data found)'
    return json_to_html({target: found_data}, depth=1)


def lists_only_space_weather_info(filename):
    """
    Generate an HTML page listing Space Weather sites information (collapsible) only.
    """
    with open(filename, 'r', encoding='utf-8') as f:
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
        <style>
            /* ====== 全体デザイン ====== */
            body {
                font-family: Arial, sans-serif;
                line-height: 1.6;
                margin: 0;
                padding: 20px;
            }
            
            h1, h2, h3 {
                margin-top: 1em;
                margin-bottom: 0.5em;
            }

            /* ====== JSON用コンテナ ====== */
            .json-container {
                margin-left: 0;
                padding-left: 0;
            }
            .json-subcontainer {
                margin-left: 20px;
            }
            .json-list {
                list-style-type: disc;
                margin-left: 40px;
            }

            /* ====== 折りたたみ要素 ====== */
            .collapsible {
                color: green;
                cursor: pointer;
                margin: 8px 0;
                user-select: none; /* テキストのドラッグ選択をしにくくする */
            }
            .collapsible:hover {
                text-decoration: underline;
            }
            .content {
                display: none;
                margin-left: 20px;
                margin-bottom: 8px;
            }
            /* 矢印切り替え */
            .collapsible.active::before {
                content: "▼ ";
            }
            .collapsible::before {
                content: "▶ ";
            }
        </style>
    </head>
    """

    body_data = (
        "<body>"
        "<h1>Space Weather Forecast Infomartion Sites Lists</h1>"
        " <br> 宇宙天気予報についてではなく<u>宇宙天気予報を実際に行う際に必要な情報について</u>個人的にまとめたものです。<br> "
        "<br> <strong>ここに記載してある一切の情報について、作者は責任を負いません。<br> "
        "また、リンク先のデータの利用条件についても十分に注意してください。</strong>"
        "<br> <br> ここに載っていない有用な宇宙天気予報関連のサイトの紹介や、手順へのアドバイス、本サイトへの意見等ありましたらこちらのIssueまでお願いしてます。"
        "<a href='https://github.com/Butadiene/SpaceWeatherForecastsInfomationTips' target='_blank'>"
        "https://github.com/Butadiene/SpaceWeatherForecastsInfomationTips</a> <br>"
        "<br> <strong> 緑色の文字はクリックすると展開できます。</strong>"
        "<h2>Information Lists</h2>"
        + list_data +
        "</body></html>"
    )
    
    script = """
    <script>
    function toggleVisibility(element) {
        element.classList.toggle("active"); // 矢印切り替え
        var content = element.nextElementSibling;
        if (content.style.display === "none" || content.style.display === "") {
            content.style.display = "block";
        } else {
            content.style.display = "none";
        }
    }
    </script>
    """
    
    html_data = head_data + body_data + script
    return html_data


def intro_space_weather(filename):
    """
    Generate an HTML page with introduction and space weather forecast tips,
    including a collapsible JSON-based site info list that shows references.
    """
    with open(filename, 'r', encoding='utf-8') as f:
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
        <style>
            body {
                font-family: Arial, sans-serif;
                line-height: 1.6;
                margin: 0;
                padding: 20px;
            }
            .json-container {
                margin-left: 0;
            }
            .json-subcontainer {
                margin-left: 20px;
            }
            .json-list {
                list-style-type: disc;
                margin-left: 40px;
            }

            .collapsible {
                color: green;
                cursor: pointer;
                margin: 8px 0;
                user-select: none;
            }
            .collapsible:hover {
                text-decoration: underline;
            }

            .content {
                display: none;
                margin-left: 20px;
                margin-bottom: 8px;
            }
            .collapsible.active::before {
                content: "▼ ";
            }
            .collapsible::before {
                content: "▶ ";
            }
        </style>
    </head>
    """

    # ===========================
    # メインの本文 (Forecast Process Template など)
    # ===========================
    body_data = (
        "<body>"
        "<h1>Tips for Space Weather Forecasting</h1>"
        "  <br> 宇宙天気予報についてではなく<u>宇宙天気予報を実際に行う際に必要な情報について</u>個人的にまとめたものです。<br> "
        "<br> <strong> ここに記載してある一切の情報について、作者は責任を負いません。<br>"
        "また、リンク先のデータの利用条件についても十分に注意してください。</strong>"
        "<br> <br> ここに載っていない有用な宇宙天気予報関連のサイトの紹介や、手順へのアドバイス、本サイトへの意見等ありましたら"
        "こちらのIssueまでお願いしてます。"
        "<a href='https://github.com/Butadiene/SpaceWeatherForecastsInfomationTips' target='_blank'>"
        "https://github.com/Butadiene/SpaceWeatherForecastsInfomationTips</a> <br>"
        "<br> <strong> 緑色の文字はクリックすると展開できます。</strong>"

        "<h2>1. Information List</h2>"
        + list_data +
        """
        <h2>2. Forecast Process Template</h2>
        <p style="color: red;">
            <strong>
            【注意】宇宙天気予報は様々なデータを俯瞰的に見て、多くの状況に応じて判断しなければならない。ここに載せるのは1テンプレートにすぎない。<br>
            また、作者は宇宙天気予報の素人であり、この手順は宇宙天気予報の学習中に作成したメモであることも明記しておく。<br>
            もしここの手順を参照して自分自身で情報解析を行う場合、必ず
            </strong>
        </p>
        """
        + get_site_info(data,"NICT 宇宙天気予報レポーㇳ") +
        """
        <p style="color: red;">
            <strong> を参照すること。 </strong>
        </p>

        <ol>
            <!-- ========================= 1.各国の予報状況 ======================= -->
            <li>
                <h3>各国の予報状況</h3>
                <p>
                    各国の予報状況を確認し、現在の太陽活動や地磁気活動がどの程度Activeかについて大まかに把握する。
                    """
        + get_site_info(data,"Present Space Weather Forecast from ISES") +
        """</p>
            </li>

            <!-- ========================= 2.太陽活動 ======================= -->
            <li>
                <h3>太陽活動</h3>
                <p>太陽風活動、地磁気活動等の根本的な要因である太陽活動の詳細を把握する。<br>
                   その後、太陽フレア、プロトンフラックスの予報を行う。</p>
                <ol>
                    <!-- 2-(1) GOESのX線フラックスの確認 -->
                    <li>
                        GOESのX線フラックスの確認
                        <p>
                            GOESのX線フラックスの直近数日の変動を確認する。GOESのX線フラックスは太陽フレアの基準となっており、
                            大まかな太陽の活動度を把握できる。<br>
                            フレアがあったかの確認、バックグラウンドの大きさと傾向（増加傾向か否かなど）の確認が重要。
                            """
        + get_site_info(data,"GOES X-ray Flux") +
        """</p>
                    </li>

                    <!-- 2-(2) プロトンフラックスの確認 -->
                    <li>
                        プロトンフラックスの確認
                        <p>
                            GOESのプロトンフラックスについての、直近数日の変動を確認する。太陽活動の活動度を把握する助けになる。
                            """
        + get_site_info(data,"GOES Proton Flux") +
        """</p>
                    </li>

                    <!-- 2-(3) 黒点全体の活動度の確認 -->
                    <li>
                        黒点全体の活動度の確認
                        <p>
                            個々の黒点について確認する前に、太陽の地球側の面に見えている黒点全体の傾向について確認する。以下の指標を確認すると良い
                        </p>
                        <ol>
                            <li>
                                F10.7(波長10.7cmの電波)の電波強度
                                <p>
                                    値だけでなく、増加傾向か減少傾向かも重要。
                                    """
        + get_site_info(data,"Solar radio flux - archive of measurements") +
        """</p>
                            </li>
                            <li>
                                太陽光球面の見えている黒点の総面積
                                <p>
                                    以下の黒点データリストに載っている面積を全部足すことで計算できる。値だけでなく、増加傾向か減少傾向かも重要。
                                    """
        + get_site_info(data,"SOLAR REGION SUMMARY") +
        """</p>
                            </li>
                            <li>
                                太陽黒点相対数
                                <p>
                                    値だけでなく、増加傾向か減少傾向かも重要。
                                    """
        + get_site_info(data,"SILSO : Daily estimated sunspot number") +
        """</p>
                            </li>
                            <li>
                                月間太陽黒点相対数
                                <p>
                                    """
        + get_site_info(data,"SILSO : Monthly relative sunspot number") +
        """</p>
                            </li>
                        </ol>
                    </li>

                    <!-- 2-(4) 太陽活動の概観を動画で確認 -->
                    <li>
                        太陽活動の概観を動画で確認
                        <p>
                            4日前からの太陽活動の動画を、波長帯ごとにざっと確認する。SDO衛星の動画を見ると良い。<br>
                            ここ4日で活動的な領域の大雑把な把握を、波長帯別に行う。<br>
                            Solar Monitorでぱっと静止画の一覧を見たあとにSDO Imagesで気になる波長を見るのがおすすめ。<br>
                            どこを見るか迷う場合、とりあえずSDOのAIA 094, 211, 304, 1600, Magnetogramあたり?
                            """
        + get_site_info(data,"Solar Monitor") +
        get_site_info(data,"SDO Images") +
        get_site_info(data,"SDO Images Dashboard") +
        """</p>
                    </li>

                    <!-- 2-(5) 活動領域(黒点近辺)の詳細を確認 -->
                    <li>
                        活動領域(≒黒点近辺)の詳細を確認
                        <p>
                            太陽表面の活動的な領域について、細かく把握していく。
                        </p>
                        <ol>
                            <!-- 2-(5)-(1) 活動領域の現況についての詳細確認 -->
                            <li>
                                活動領域(≒黒点近辺)の現況についての詳細な確認
                                <p>
                                    太陽表面の活動的な領域の現況について、細かく把握する。
                                </p>
                                <ol>
                                    <li>
                                        東端から回り込んでくる活動領域の確認
                                        <p>
                                            SDO画像の094などを見て東端から回り込んできた、あるいは回り込んできそうな位置にある、
                                            黒点や活動的な領域を確認する。<br>
                                            特に、094などで東端にコロナの噴出が見えたり、304でフィラメントの吹き飛びが見える場合は着目する。
                                            """
        + get_site_info(data,"SDO Images") +
        """</p>
                                    </li>
                                    <li>
                                        黒点位置と番号の確認
                                        <p>
                                            太陽表面に出ている黒点とそれに振られている番号を確認する。<br>
                                            また、先程確認した東端の活動のうち未採番のものがあった場合、それについて認識する。
                                            """
        + get_site_info(data,"SOHO Sunspots") +
        """</p>
                                    </li>
                                    <li>
                                        各活動領域のデータを確認
                                        <p>
                                            以下のリストを見て、各活動領域のタイプ分け、面積、黒点数などを確認。<br>
                                            この時、前日から各活動領域はどのように変化したのか（面積は増えたか、磁場構造は変わったか）を確認するのが重要。<br>
                                            前日と比べてリストから消えた活動領域は、西端を越えて裏側に回り込んだのか、衰退したのかの判定をする必要がある。
                                            """
        + get_site_info(data,"SOLAR REGION SUMMARY") +
        """</p>
                                    </li>
                                    <li>
                                        イベントリストを確認
                                        <p>
                                            各活動領域がどのぐらいの規模、数のフレアを起こしたかを確認する。以下のリストを使用すると良い。<br>
                                            また、イベントリストの確認の際にX線フラックスを突き合わせる。(LMSALはイベントの登録に1日前後の遅れが生じることがあるため)
                                            """
        + get_site_info(data,"LMSAL last event reports") +
        """<br>
                                            また、イベントリストの確認の際にX線フラックスを突き合わせる。
                                            """
        + get_site_info(data,"GOES X-ray Flux") +
        """</p>
                                    </li>
                                </ol>
                            </li>
                            <!-- 2-(5)-(2) 各活動領域でのフレア予報の確認 -->
                            <li>
                                各活動領域でのフレア予報の確認
                                <p>
                                    各活動領域で今後フレアが発生するかどうかについて、モデルによる予測を確認する。Deep Flare NetのDeFN-Rを参照すると良い。
                                    """
        + get_site_info(data,"Deep Flare Net") +
        """</p>
                            </li>
                        </ol>
                    </li>

                    <!-- 2-(6) 注目すべき活動領域の詳細確認 -->
                    <li>
                        注目すべき活動領域について、より細かく詳細を確認。
                        <p>
                            上で得た各活動領域の詳細から、活動的、あるいは活動的な可能性がある活動領域をリストアップし、それらについて以下の手順でさらなる詳細を把握していく。
                        </p>
                        <ol>
                            <!-- (a) 磁場構造の詳細把握 -->
                            <li>
                                磁場構造の詳細な把握
                                <p>
                                    SHARPを用いて、着目すべき活動領域の磁場構造を把握する。特にシア構造や磁力線の浮上などに着目。<br>
                                    SOLAR REGION SUMMARYでβ型と書いてあった黒点が実際よく見たらδ型、ということもあったりする。
                                    """
        + get_site_info(data, "SHARP Vector Magnetograms") +
        get_site_info(data, "SHARP Data Viewer") +
        """</p>
                            </li>
                            <!-- (b) 太陽活動の動画の見直し -->
                            <li>
                                太陽活動の動画の見直し
                                <p>
                                    リストアップした各活動領域に着目しながら、太陽表面の動画を見直す。<br>
                                    特に、AIA 094やAIA 1600でチカチカ光る光(磁場の浮上を示唆)、活動領域付近のフレアなどをもう一度確認。
                                    """
        + get_site_info(data,"SDO Images") +
        get_site_info(data,"SDO Images Dashboard") +
        get_site_info(data,"LMSAL last event reports") +
        """</p>
                            </li>
                        </ol>
                    </li>

                    <!-- 2-(7) フレア予報を考える -->
                    <li>
                        フレア予報を考える。
                        <p>
                            これまで得た各活動領域の情報を考慮しながら、太陽フレアの予報を考える。<br>
                            <strong>Mクラス以上</strong>のフレアを起こす可能性がある活動領域が存在するか、を基準に考えると良い。Deep Flare Netも助けになる。
                            """
        + get_site_info(data,"Deep Flare Net") +
        """<br>
                            また、SYNOPTIC MAPの予報を参考にしてみても良いかもしれない。
                            """
        + get_site_info(data,"SOLAR SYNOPTIC MAP") +
        """</p>
                    </li>

                    <!-- 2-(8) プロトン現象の予報 -->
                    <li>
                        プロトン現象の予報を考える。
                        <p>
                            プロトン現象の予報について考える。プロトン現象は太陽フレアの発生に強く依存するため、
                            太陽フレアの予報、特にMクラスフレアの発生を目安に考えると良い。<br>
                            また、プロトンフラックスの現況も踏まえる必要がある。
                            """
        + get_site_info(data,"GOES Proton Flux") +
        """</p>
                    </li>
                </ol>
            </li>

            <!-- ========================= 3.太陽風活動 ======================= -->
            <li>
                <h3>太陽風活動</h3>
                <p>
                    地磁気擾乱の予報の大前提となる、太陽風活動の把握を行う。
                </p>
                <ol>
                    <!-- 3-(1) L1地点での太陽風の現況 -->
                    <li>
                        L1地点での太陽風の現況把握
                        <p>
                            L1地点での太陽風の現況把握を行う。これにより地球近辺にどのような太陽風が到来しているかがわかる。<br>
                            現在の値はもちろん、上昇傾向か否かなどのトレンドを把握するのも重要。
                            """
        + get_site_info(data,"SWPC REAL TIME SOLAR WIND") +
        """</p>
                    </li>

                    <!-- 3-(2) 高エネルギープラズマの現況把握(ACE EPAMなど) -->
                    <li>
                        L1地点での高エネルギープラズマの現況把握
                        <p>
                            太陽風とともに飛んでくるプラズマのうち、数十KeVから数MeVのものについての把握を行う。(EPAMを見る)
                            """
        + get_site_info(data,"ACE REAL TIME SOLAR WIND") +
        """</p>
                    </li>

                    <!-- 3-(3) コロナホールと高速太陽風の把握 -->
                    <li>
                        コロナホールと高速太陽風の把握
                        <p>コロナホールとそれにより飛来する高速太陽風についての把握を行う。</p>
                        <ol>
                            <li>
                                コロナホールの確認
                                <p>
                                    SDO衛星のAIA 211の画像などから、太陽表面に存在するコロナホールを確認し、リスト化する。<br>
                                    Solar Monitor、SOLAR SYNOPTIC MAPも活用し、コロナホール内部の磁場極性(+/-)もチェックする。
                                    """
        + get_site_info(data,"SDO Images") +
        get_site_info(data,"Solar Monitor") +
        get_site_info(data,"SOLAR SYNOPTIC MAP") +
        """</p>
                            </li>
                            <li>
                                L1地点での太陽風変動が高速太陽風によるものかを判断
                                <p>
                                    L1地点で高速太陽風が来ているかを判断する。太陽風速度やACE EPAMデータなどを確認する。<br>
                                    (ソースとなるコロナホールとの磁場極性も突き合わせる)
                                    """
        + get_site_info(data,"SWPC REAL TIME SOLAR WIND") +
        get_site_info(data,"ACE REAL TIME SOLAR WIND") +
        get_site_info(data,"SDO Images") +
        get_site_info(data,"Solar Monitor") +
        get_site_info(data,"SOLAR SYNOPTIC MAP") +
        """</p>
                            </li>
                            <li>
                                1太陽周期前の太陽風、コロナホールの確認
                                <p>
                                    1太陽周期前(27日前)の太陽表面の画像と、太陽風のデータを確認。<br>
                                    類似のコロナホールがあり、太陽風の値が同様に変化していれば予報に役立つ可能性がある。
                                    """
        + get_site_info(data,"Solar Monitor") +
        get_site_info(data,"SDO Images") +
        get_site_info(data,"SWPC REAL TIME SOLAR WIND") +
        """</p>
                            </li>
                            <li>
                                シミュレーションの確認
                                <p>
                                    数値シミュレーションによる予測を見る。
                                    """
        + get_site_info(data,"Solar Wind Simulation") +
        """</p>
                            </li>
                            <li>
                                高速太陽風とコロナホールに関する現況把握
                                <p>
                                    以上の情報を複合して、「現在高速太陽風が到来中か、今後到来する可能性が高いか」などを判断。
                                </p>
                            </li>
                        </ol>
                    </li>

                    <!-- 3-(4) CMEの把握 -->
                    <li>
                        CMEの把握
                        <p>
                            CMEが発生しているか、到来しているかの把握を行う。様々なデータから複合的に判断が必要。
                        </p>
                        <ol>
                            <li>
                                SDO画像から、CME候補となる現象の確認
                                <p>
                                    高エネルギー帯で見えるコロナの吹き飛び(AIA 094などで見えるDimming)や304でのフィラメント吹き飛びが目安になる。
                                    """
        + get_site_info(data,"SDO Images") +
        get_site_info(data,"SDO Images Dashboard") +
        get_site_info(data,"A Heliophysics Events Knowledgebase") +
        """</p>
                            </li>
                            <li>
                                LASCO画像による宇宙空間への放出確認
                                <p>
                                    SOHO衛星のコロナグラフ(LASCO C2/C3)でCMEの可視化を確認。<br>
                                    フルハローCMEの有無なども注目。
                                    """
        + get_site_info(data,"SOHO LASCO C2 & C3") +
        get_site_info(data,"SOHO LASCO C2 & C3 Diff and mesurement") +
        """<br>
                                    CACTUSの自動検出カタログも簡易チェックに使える。
                                    """
        + get_site_info(data,"CACTUS Auto-CME-catalog") +
        """</p>
                            </li>
                            <li>
                                CMEのリストアップ
                                <p>
                                    SDOでの発生時刻とLASCOでのコロナ噴出時刻を付き合わせ、CMEとしてリストアップ。<br>
                                    裏側発生は地球に来ない可能性なども検討する。
                                    """
        + get_site_info(data,"Solar and geophysical events") +
        """</p>
                            </li>
                            <li>
                                CMEの速度計算
                                <p>
                                    地球に到来する可能性があるCMEの速度をLASCOなどで計測し、
                                    到達時間を推定する。
                                    """
        + get_site_info(data,"SOHO LASCO C2 & C3") +
        get_site_info(data,"SOHO LASCO C2 & C3 Diff and mesurement") +
        """</p>
                            </li>
                            <li>
                                太陽風観測データとCMEの対応確認
                                <p>
                                    予想到達時間を迎えたCMEが実際に到着したか、SWPCやACEなどのリアルタイム太陽風データを確認。
                                    """
        + get_site_info(data,"SWPC REAL TIME SOLAR WIND") +
        get_site_info(data,"ACE REAL TIME SOLAR WIND") +
        """</p>
                            </li>
                            <li>
                                シミュレーションとの対応確認
                                <p>
                                    シミュレーションがCMEの到来をどう予測しているか。
                                    """
        + get_site_info(data,"Solar Wind Simulation") +
        """</p>
                            </li>
                        </ol>
                    </li>
                </ol>
            </li>

            <!-- ========================= 4.地磁気擾乱 ======================= -->
            <li>
                <h3>地磁気擾乱</h3>
                <p>
                    地磁気擾乱に関する現況を把握し、予報を行う。<br>
                    太陽風の予報精度が低いため、地磁気擾乱の予報も難しいことが多い。
                </p>
                <ol>
                    <li>
                        現在の地磁気活動度の把握
                        <p>
                            現在のK指数やKp指数を把握する。
                            """
        + get_site_info(data,"SWPC PLANETARY K-INDEX") +
        get_site_info(data,"KAKIOKA K-INDEX") +
        """<br>
                            GOES MAGNETOMETERで磁気圏の圧縮具合を推測することもある。
                            """
        + get_site_info(data,"GOES MAGNETOMETER") +
        """</p>
                    </li>
                    <li>
                        24時間前から現在までの地磁気活動の把握
                        <p>
                            K指数やKp指数の変化を見て、24時間での最大値や合計値に着目。
                            """
        + get_site_info(data,"SWPC PLANETARY K-INDEX") +
        get_site_info(data,"KAKIOKA K-INDEX") +
        """</p>
                    </li>
                    <li>
                        オプション: 磁気嵐やサブストームの確認
                        <ol>
                            <li>
                                (地磁気が大きく荒れている場合) DST指数の確認
                                <p>
                                    DST指数が-30nT ~ -50nT以下だと磁気嵐と呼ばれることが多い。
                                    """
        + get_site_info(data,"DST-INDEX") +
        """</p>
                            </li>
                            <li>
                                (サブストームの発生が気になる場合) AE指数の確認
                                <p>
                                    AE指数はサブストームなど高緯度帯での磁場乱れを把握するのに役立つ。
                                    """
        + get_site_info(data,"AE index") +
        """</p>
                            </li>
                        </ol>
                    </li>
                    <li>
                        地磁気擾乱の予報を行う
                        <p>
                            現在の地磁気活動度、太陽風の現況・今後の予測などを踏まえ、地磁気擾乱の予報を行う。<br>
                            南向きの強い磁場が到来すると激しい地磁気擾乱になる可能性があるなど。
                        </p>
                    </li>
                </ol>
            </li>

            <!-- ========================= 5.放射線帯 ======================= -->
            <li>
                <h3>放射線帯</h3>
                <p>
                    放射線帯に関する現況を把握し、予報を行う。<br>
                    宇宙天気予報としては静止軌道付近のMeV電子(外帯)に注目することが多い。
                </p>
                <ol>
                    <li>
                        放射線帯の現況の把握
                        <p>
                            静止軌道付近での電子24時間fluenceとfluxを確認する。
                        </p>
                        <ol>
                            <li>
                                静止軌道における、電子の24時間fluenceの把握
                                <p>
                                    GOESやひまわりのデータ、特にGOESの24時間fluenceは放射線帯全体の活動度を把握する指標として有用。
                                    """
        + get_site_info(data,"NICT GOES Electron Fluences and flux") +
        get_site_info(data,"HIMAWARI SEDA DATA VIEWER") +
        """</p>
                            </li>
                            <li>
                                静止軌道における、電子fluxの把握
                                <p>
                                    GOESやひまわりの電子fluxはより短時間・局所的な変動を見るのに有用。
                                    """
        + get_site_info(data,"NOAA GOES Electron Flux") +
        get_site_info(data,"HIMAWARI SEDA DATA VIEWER") +
        """</p>
                            </li>
                            <li>
                                fluence予報の確認
                                <p>
                                    24時間fluenceの予測モデルを確認する。
                                    """
        + get_site_info(data,"Electron fluences forecast") +
        """</p>
                            </li>
                            <li>
                                flux予報の確認
                                <p>
                                    モデルによる各衛星ごとの電子flux予報。
                                    """
        + get_site_info(data,"静止軌道危険度予測") +
        """</p>
                            </li>
                        </ol>
                    </li>
                    <li>
                        放射線帯電子予報を行う
                        <p>
                            太陽風の予測、地磁気擾乱の予測等も踏まえ、放射線帯電子の予報を考える。<br>
                            大きな地磁気擾乱が起きると一時的に外帯の電子が減る場合もあるが、その後加速されて増えることもある。
                        </p>
                    </li>
                </ol>
            </li>

            <!-- ========================= 6.電離圏擾乱 ======================= -->
            <li>
                <h3>電離圏擾乱</h3>
                <p>
                    電離圏擾乱に関する現況を把握し、予報を行う。<br>
                    電離圏は地域性が大きいため、ローカルに解析する必要があることに注意。
                </p>
                <ol>
                    <li>
                        デリンジャー現象の現況を把握する
                        <p>
                            イオノグラムなどから把握できる。
                            """
        + get_site_info(data,"NICT Site Ionogram Viewer") +
        get_site_info(data,"Observed foEs") +
        get_site_info(data,"Dellinger phenomenon") +
        """</p>
                    </li>
                    <li>
                        デリンジャー現象の予報を考える
                        <p>
                            デリンジャー現象はX線フレアによって起こるため、太陽フレア(Mクラス以上)の発生に着目。
                        </p>
                    </li>
                    <li>
                        スポラティックE層の現況を把握する
                        <p>
                            スポラティックE層はイオノグラムで確認する。
                            """
        + get_site_info(data,"NICT Site Ionogram Viewer") +
        get_site_info(data,"Observed foEs") +
        """</p>
                    </li>
                    <li>
                        電離圏嵐の現況を把握する
                        <p>
                            電離圏での電子密度(foF2, TEC)などを地域ごとに把握する。
                            """
        + get_site_info(data,"foF2 and GEONET TEC time change at Japan") +
        get_site_info(data,"GEONET TEC map") +
        """</p>
                    </li>
                    <li>
                        電離圏嵐の予報を考える
                        <p>
                            地磁気擾乱や太陽風の予報が難しいため、電離圏嵐の予報も難しい。<br>
                            今後の地磁気活動と電離圏の現況を踏まえておおまかに予想するのみ。
                        </p>
                    </li>
                </ol>
            </li>

            <!-- ========================= 7.専門機関の予報との照らし合わせ ======================= -->
            <li>
                <h3>専門機関の予報との照らし合わせ</h3>
                <p>
                    専門機関の出している予報レポートをもう一度確認する。
                    """
        + get_site_info(data,"NICT 宇宙天気予報レポーㇳ") +
        get_site_info(data,"Present Space Weather Forecast from ISES") +
        """</p>
            </li>
        </ol>
        """
    )

    tail_data = "</body></html>"

    script = """
    <script>
    function toggleVisibility(element) {
        element.classList.toggle("active"); // 矢印切り替え用
        var content = element.nextElementSibling;
        if (content.style.display === "none" || content.style.display === "") {
            content.style.display = "block";
        } else {
            content.style.display = "none";
        }
    }
    </script>
    """

    html_data = head_data + body_data + tail_data + script
    return html_data


# =========================
# 実行例 (メイン処理部分)
# =========================

# Example usage:
info_html_data = intro_space_weather('./Datas/space_weather_info.json')
with open('./docs/index.html', 'w') as f:
    f.write(info_html_data)
with open('./docs_info_tips/space_weather_info.html', 'w') as f:
    f.write(info_html_data)


lists_only_html_data = lists_only_space_weather_info('./Datas/space_weather_info.json')
with open('./docs_info_lists/space_weather_info_lists.html', 'w') as f:
    f.write(lists_only_html_data)
