from dataclasses import dataclass

from flask import Flask, jsonify
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

    UniqueConstraint('city_id', 'weather_data_id', name='city_weather_unique')


@app.route('/api/weatherdata')
def index():
    return jsonify(WeatherData.query.all())


# @app.route('/api/weatherdata/<str:name>/', methods=['POST'])
# def city(name):
#     # TODO: get random city and display some weather info for it\
#     req = requests.get('')
#     pass


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
