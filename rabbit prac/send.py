import pika

# Connect to RabbitMQ server
connection = pika.BlockingConnection(
    pika.ConnectionParameters('localhost')
)

channel = connection.channel()

# Create queue
channel.queue_declare(queue='hello', durable=True)

# Send message
message = "Hello, RabbitMQ!"

channel.basic_publish(
    exchange='',
    routing_key='hello',
    body=message
)

print(f" [x] Sent '{message}'")

connection.close()