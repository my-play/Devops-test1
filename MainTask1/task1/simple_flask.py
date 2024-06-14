from flask import Flask, jsonify
import requests
import json

app = Flask(__name__)


def get_Chuck_joke(api_url):
    response = requests.get(api_url)
    data = response.json()
    return data['value']


def load_config():
    with open('config.json', 'r') as file:
        config = json.load(file)
        return config


@app.route('/')
def joke_from_Chuck():
    config = load_config()
    api_url = config['api_url']
    joke = get_Chuck_joke(api_url)
    return jsonify({'joke': joke})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5999)
