import pika
import json

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

uploads_dir = '../uploads/'
upload_msg = {
    'file_name': 'ul.mp3',
    'user_id': '1234',
    'user_name': 'John Smith',
}

# Publish the message to the exchange.
#   - Persistent delivery mode.
channel.basic_publish(exchange='music_player.upload.fanout',
                      routing_key='', body=json.dumps(upload_msg),
                      properties=pika.BasicProperties(
                          delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE
                      ))

print("Sent message to process music file.")
connection.close()
