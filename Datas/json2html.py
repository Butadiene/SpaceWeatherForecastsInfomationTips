import json

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
    """
        <li>Item 1</li>
        <li>Item 2</li>
        <li>Item 3</li>

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
