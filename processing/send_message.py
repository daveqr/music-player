import pika
import json

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

uploads_dir = '../uploads/'
upload_meta = {
    'file_name': 'ul.mp3',
    'user_id': '1234',
    'user_name': 'John Smith',
}

# Publish the message to the exchange
channel.basic_publish(exchange='music_player.upload.fanout',
                      routing_key='', body=json.dumps(upload_meta))

print("Sent message to process music file.")
connection.close()
