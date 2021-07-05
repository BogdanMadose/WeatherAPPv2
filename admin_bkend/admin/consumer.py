import pika

params = pika.URLParameters('amqps://sayiodnr:2qhuhCqq7IEvklKrjpDpggZ4b5dI04sb@goose.rmq2.cloudamqp.com/sayiodnr')

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='admin')


def callback(ch, method, properties, body):
    print('Recieved in admin')
    print(body)


channel.basic_consume(queue='admin', on_message_callback=callback, auto_ack=True)

print('Started consuming')

channel.start_consuming()
channel.close()
