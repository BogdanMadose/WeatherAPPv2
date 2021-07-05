import json

import pika

from main import WeatherData, db

params = pika.URLParameters('amqps://sayiodnr:2qhuhCqq7IEvklKrjpDpggZ4b5dI04sb@goose.rmq2.cloudamqp.com/sayiodnr')

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='main')


def callback(ch, method, properties, body):
    print('Recieved in main')
    data = json.loads(body)
    print(data)

    if properties.content_type == 'weather_data_created':
        weather_data = WeatherData(id=data['id'],
                                   temp=data['temp'],
                                   wind_speed=data['wind_speed'],
                                   pressure=data['pressure'])
        db.session.add(weather_data)
        db.session.commit()
        print('Weather Data inserted')
    elif properties.content_type == 'weather_data_updated':
        weather_data = WeatherData.query.get(data['id'])
        weather_data.temp = data['temp']
        weather_data.wind_speed = data['wind_speed']
        weather_data.pressure = data['pressure']
        db.session.commit()
        print('Weather Data changed')
    elif properties.content_type == 'weather_data_deleted':
        weather_data = WeatherData.query.get(data)
        db.session.delete(weather_data)
        db.session.commit()
        print('Weather Data deleted')


channel.basic_consume(queue='main', on_message_callback=callback, auto_ack=True)

print('Started consuming')

channel.start_consuming()
channel.close()
