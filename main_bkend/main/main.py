import json
from dataclasses import dataclass
import requests
from flask import Flask, jsonify, abort
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import UniqueConstraint

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql://root:root@db/main'
CORS(app)

db = SQLAlchemy(app)


@dataclass
class WeatherData(db.Model):
    id: int
    temp: int
    wind_speed: float
    pressure: int

    id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    temp = db.Column(db.Integer)
    wind_speed = db.Column(db.Float)
    pressure = db.Column(db.Integer)


@dataclass
class WeatherDataCities(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    weather_id = db.Column(db.Integer)
    city_id = db.Column(db.Integer)
    city_name = db.Column(db.String(200))
    temp = db.Column(db.Integer)
    wind_speed = db.Column(db.Float)
    pressure = db.Column(db.Integer)

    UniqueConstraint('city_id', 'weather_id', name='city_weather_unique')


@app.route('/api/weatherdata')
def index():
    return jsonify(WeatherData.query.all())


@app.route('/api/weatherdata/<string:name>/display', methods=['POST'])
def get_weather(name):
    req = requests.get(f"http://host.docker.internal:8000/api/city/" + name)
    data = req.json()

    try:
        weather_city = WeatherDataCities(weather_id=data['weather_id'],
                                         city_name=name,
                                         city_id=data['city_id'],
                                         temp=data['temp'],
                                         wind_speed=data['wind_speed'],
                                         pressure=data['pressure'])
        db.session.add(weather_city)
        db.session.commit()

        # TODO: rabbit log
        # TODO: SQL Exception handling
    except:
        abort(400, 'Wrong city')

    return jsonify({
        'message': 'weather data displayed'
    })


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
