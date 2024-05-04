# server/server.py
import pika
import json
from db.database import add_department, add_employee, search_employees_by_department

def on_request(ch, method, properties, body):
    request = json.loads(body)
    response = None

    if request['command'] == 'add_department':
        response = add_department(request['name'], request['location'])
    elif request['command'] == 'add_employee':
        response = add_employee(request['name'], request['position'], request['salary'], request['department_id'])
    elif request['command'] == 'search_by_department':
        response = search_employees_by_department(request['department_name'])

    ch.basic_publish(exchange='',
                     routing_key=properties.reply_to,
                     properties=pika.BasicProperties(correlation_id=properties.correlation_id),
                     body=json.dumps(response))
    ch.basic_ack(delivery_tag=method.delivery_tag)

def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='SRV.Q')
    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue='SRV.Q', on_message_callback=on_request)

    print("Awaiting RPC requests")
    channel.start_consuming()

if __name__ == "__main__":
    main()
