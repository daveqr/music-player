import pika
import json


def callback(ch, method, properties, body):
    music_json = json.loads(body)
    file_name = music_json['file_name']

    print(f"Processing {file_name}")

    # Acknowledge the message to remove it from the queue.
    ch.basic_ack(delivery_tag=method.delivery_tag)


connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.basic_consume(queue='music_player.track.process',
                      on_message_callback=callback)

# One message to a worker at a time.
channel.basic_qos(prefetch_count=1)

print('Worker is waiting for messages. To exit, press Ctrl+C')
channel.start_consuming()
