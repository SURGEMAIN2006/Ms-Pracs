import pika

# Function to receive message
def callback(ch, method, properties, body):
    print(f" [x] Received {body}")

# Connect to RabbitMQ server
connection = pika.BlockingConnection(
    pika.ConnectionParameters('localhost')
)

channel = connection.channel()

# Create the same queue
channel.queue_declare(queue='hello', durable=True)

# Receive messages
channel.basic_consume(
    queue='hello',
    on_message_callback=callback,
    auto_ack=True
)

print(' [*] Waiting for messages. To exit, press CTRL+C')

channel.start_consuming()