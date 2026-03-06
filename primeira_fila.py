import pika

print(" Conectando ao RabbitMQ...")

# Conecta
connection = pika.BlockingConnection(
    pika.ConnectionParameters(
        host='localhost',
        credentials=pika.PlainCredentials('guest', 'guest')
    )
)
channel = connection.channel()

# Cria uma fila
channel.queue_declare(queue='minha_primeira_fila')
print(" Fila criada!")

# Envia mensagem
channel.basic_publish(
    exchange='',
    routing_key='minha_primeira_fila',
    body='Olá RabbitMQ! Minha primeira fila!'
)
print(" Mensagem enviada!")

# Recebe a mensagem
method_frame, header_frame, body = channel.basic_get('minha_primeira_fila')
if method_frame:
    print(f" Mensagem recebida: {body.decode()}")
    channel.basic_ack(method_frame.delivery_tag) 
    print(" Mensagem confirmada!")
else:
    print(" Nenhuma mensagem na fila")

connection.close()