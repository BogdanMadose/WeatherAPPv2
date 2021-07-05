import json

import pika

params = pika.URLParameters('amqps://sayiodnr:2qhuhCqq7IEvklKrjpDpggZ4b5dI04sb@goose.rmq2.cloudamqp.com/sayiodnr')

connection = pika.BlockingConnection(params)

channel = connection.channel()


def publish(method, body):
    properties = pika.BasicProperties(method)
    message = json.dumps(body)
    channel.basic_publish(exchange='', routing_key='main', body=message, properties=properties)
