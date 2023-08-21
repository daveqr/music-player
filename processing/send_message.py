import pika
import json

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='music_player.track.process')
music_file = 'path/to/music.mp3'
music_json = {
    'file_name': 'music.mp3'
}
message_body = json.dumps(music_json)

channel.basic_publish(
    exchange='',
    routing_key='music_player.track.process',
    body=message_body,
    properties=pika.BasicProperties(
        delivery_mode=2, # QoS level 2
        content_type='application/json'
    )
)
print("Sent message to process music file.")
connection.close()
