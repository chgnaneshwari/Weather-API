from flask import Flask, jsonify
import requests
import json
import xmltodict

app = Flask(__name__)

@app.route('/get_weather/<station_id>')
def get_weather(station_id):
    try:
        url = f'https://forecast.weather.gov/xml/current_obs/{station_id}.xml'
        response = requests.get(url)

        if response.status_code != 200:
            return jsonify({
                'error': f'Invalid station ID: {station_id}. HTTP Status {response.status_code}',
                'message': response.text
            }), response.status_code
        
        xml_data = response.content
        json_data = xmltodict.parse(xml_data)
        
        return jsonify(json_data)

    except Exception as e:
        return jsonify({'error': str(e), 'message': 'Check station ID and try again'}), 500

@app.route('/')
def health_check():
    return 'I am alive!'

if __name__ == '__main__':
    app.run(debug=True)
