"""
from flask quickstart:
http://flask.pocoo.org/docs/1.0/quickstart/

To run the API server, run the file:
python api_demo.py

Then either visit the url, use curl, or requests to get the data:

http://127.0.0.1:5000/hello_world

To retrieve the data, visit:

http://127.0.0.1:5000/weather_data
"""
from pymongo import MongoClient

from flask import Flask
app = Flask(__name__)

@app.route('/hello_world')
def hello_world():
    return 'Hello, World!'

@app.route('/weather_data')
def weather_data():
    client = MongoClient()
    db = client['weather_test']
    denver_weather = db['denver']
    data = str(list(denver_weather.find()))
    client.close()

    return data


if __name__ == "__main__":
    app.run()
