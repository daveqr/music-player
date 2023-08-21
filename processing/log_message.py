import pika
import json
import argparse
from datetime import datetime
from logging_strategy import TextFileLoggingStrategy, ConsoleLoggingStrategy

parser = argparse.ArgumentParser(
    description='Log file upload messages them.')

parser.add_argument('--strategy', type=str,
                    default='file', choices=['file', 'db', 'console'])

args = parser.parse_args()


def callback(ch, method, properties, body):
    upload_msg = json.loads(body)

    if args.strategy == 'file':
        logging_strategy = TextFileLoggingStrategy()
    elif args.strategy == 'console':
        logging_strategy = ConsoleLoggingStrategy()        
    # elif args.strategy == 'db':
    #     logging_strategy = DbLoggingStrategy()
    else:
        raise ValueError(f"Unsupported logging strategy: {args.strategy}")

    logging_strategy.log(upload_msg)

    # Acknowledge the message to remove it from the queue
    ch.basic_ack(delivery_tag=method.delivery_tag)

    print(f"Logging {upload_msg['file_name']}")


connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.basic_consume(queue='music_player.track.log',
                      on_message_callback=callback)

print('Worker is waiting for messages. To exit, press Ctrl+C')
channel.start_consuming()
