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
    f"""
    <h2> Forecast Process Template </h2>
    <p style="color: red;">Warning: 宇宙天気予報は様々なデータを俯瞰的に見て、多くの状況に応じて判断しなければならない。ここに載せるのは1テンプレートにすぎない。</p>

    <ol>
        <li>
            各国の予報状況
            <p>各国の予報状況を確認し、現在の太陽活動や地磁気活動がどの程度Activeかをぼんやり把握する。{get_site_info(data,"Space weather forecast for each country")}</p>
        </li>
        <li>
            太陽活動
            <p>太陽風活動、地磁気活動等の根本的な要因である太陽活動の詳細を把握する。</p>
            <ol>
                <li>
                    GOESのX線フラックスの確認
                    <p>GOESのX線フラックスの直近数日の変動を確認する。GOESのX線フラックスは太陽フレアの基準となっており、大まかな太陽の活動度を把握できる。また大きなフレアがあったかも確認できる。{get_site_info(data,"GOES X-ray Flux")}</p>
                </li>
                <li>
                    黒点全体の活動度の確認
                    <p>個々の黒点について確認する前に、太陽の地球側の面に見えている黒点全体の傾向について確認する。以下の指標を確認すると良い</p>
                    <ol>
                        <li>
                            F10.7(波長10.7cmの電波)の電波強度
                            <p>以下参考。値だけでなく増加傾向か減少傾向かも重要。{get_site_info(data,"DRAO")} </p>
                        </li>   
                        <li>
                            太陽光球面の見えている黒点の総面積
                            <p>以下の黒点データリストに載っている面積を全部足すことで計算できる。値だけでなく増加傾向か減少傾向かも重要。{get_site_info(data,"SOLAR REGION SUMMARY")}</p>
                        </li>
                        <li>
                            太陽黒点相対数
                            <p>以下参考。値だけでなく増加傾向か減少傾向かも重要。{get_site_info(data,"SILSO : Daily estimated sunspot number")}</p>
                        </li>
                        <li>
                            月間太陽黒点相対数
                            <p>以下参考。{get_site_info(data,"SILSO : Monthly relative sunspot number")}</p>
                        </li>                        
                    </ol>
                </li>
                    太陽活動の動画を確認
                    <p></p>
            </ol>
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
html_data = intro_space_weather('./Datas/space_weather_info.json')
with open('./Datas/space_weather_info.html', 'w') as f:
    f.write(html_data)
