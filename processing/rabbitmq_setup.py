import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declare the exchange
exchange_name = 'file_upload_exchange'
channel.exchange_declare(
    exchange='file_upload_exchange', exchange_type='fanout')

# Declare the processing queue and bind it to the exchange
processing_queue_name = 'music_player.track.process'
channel.queue_declare(queue=processing_queue_name)
channel.queue_bind(exchange=exchange_name, queue=processing_queue_name)

# Declare the logging queue and bind it to the exchange
logging_queue_name = 'music_player.track.log'
channel.queue_declare(queue=logging_queue_name)
channel.queue_bind(exchange=exchange_name, queue=logging_queue_name)

connection.close()