
from flask import Flask, jsonify, render_template
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)



## div 요소의 class를 반환
def check_class_in_page(url, class_name):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')

        # Check if the class_name exists in any div element
        return any(class_name in div.get('class', []) for div in soup.find_all('div'))
    except requests.exceptions.RequestException as e:
        print(f"Request error for URL {url}: {e}")
    except Exception as e:
        print(f"Error checking class for URL {url}: {e}")
    return False

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/check-status')
def check_alerts_border():
    urls = {
        'site_name_1': 'site_url_1',

    }
    class_name = 'good-border'
    results = {key: not check_class_in_page(url, class_name) for key, url in urls.items()}
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)

