from flask import Flask, jsonify, request
import requests, os 
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

RAPIDAPI_KEY = os.getenv("RAPIDAPI_KEY")
RAPIDAPI_HOST = os.getenv("RAPIDAPI_HOST")

@app.route('/weather', methods=['GET'])
def get_weather():
    city = request.args.get('city', 'Cairo')
    if not city:
        return jsonify({"error": "City parameter is required"}), 400

    url = f"https://{RAPIDAPI_HOST}/current.json?q={city}"
    headers = {
        "X-RapidAPI-Key": RAPIDAPI_KEY,
        "X-RapidAPI-Host": RAPIDAPI_HOST
    }
    response = requests.get(url, headers=headers)
    return jsonify(response.json())
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
