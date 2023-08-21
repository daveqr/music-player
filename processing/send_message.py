import pika
import json

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()



music_file = 'path/to/music.mp3'
music_json = {
    'file_name': 'music.mp3'
}
message_body = json.dumps(music_json)

# Publish the message to the exchange
channel.basic_publish(exchange=exchange_name, routing_key='', body=message_body)

print("Sent message to process music file.")
connection.close()
