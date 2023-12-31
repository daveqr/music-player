import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declare the exchange.
exchange_name = 'music_player.upload.fanout'
channel.exchange_declare(
    exchange='music_player.upload.fanout', exchange_type='fanout')

# Declare the processing queue and bind it to the exchange.
#   - durable
processing_queue_name = 'music_player.track.process'
channel.queue_declare(queue=processing_queue_name, durable=True)
channel.queue_bind(exchange=exchange_name, queue=processing_queue_name)

# Declare the logging queue and bind it to the exchange.
#   - durable
logging_queue_name = 'music_player.track.log'
channel.queue_declare(queue=logging_queue_name, durable=True)
channel.queue_bind(exchange=exchange_name, queue=logging_queue_name)

connection.close()