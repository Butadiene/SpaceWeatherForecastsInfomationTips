import json

def json_to_html(data, depth=0):
    html = ''
    spacing = '  ' * depth

    # Determine font size based on depth
    font_size = 20

    # If the data is a dictionary, convert each key-value pair to HTML
    if isinstance(data, dict):

        html += f'<div style="margin-left:20px; font-size: {font_size-depth*1.5}">'
        for key, value in data.items():
            if isinstance(value, (dict, list)):
                if depth > 0:  # Only make the topmost object collapsible
                    html += f'{spacing}<div class="collapsible"  style="color: green;" onclick="toggleVisibility(this)"><strong>{key}</strong></div>'
                    html += f'<div class="content" style="display: none;">{json_to_html(value, depth+1)}</div>'
                else:
                    html += f'{spacing}<strong>{key}:</strong> {json_to_html(value, depth+1)}'
            else:
                if "URL" in key and is_url(value):
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

def convert_json_file_to_html(filename):
    with open(filename, 'r') as f:
        data = json.load(f)
    html_data = json_to_html(data)

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

    return script + html_data

# Example usage:
html_data = convert_json_file_to_html('./Datas/space_weather_info.json')
with open('./Datas/space_weather_info.html', 'w') as f:
    f.write(html_data)
