# client/client.py
import pika
import json
import uuid

class RpcClient:
    def __init__(self):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
        self.channel = self.connection.channel()

        result = self.channel.queue_declare(queue='', exclusive=True)
        self.callback_queue = result.method.queue

        self.channel.basic_consume(queue=self.callback_queue,
                                   on_message_callback=self.on_response,
                                   auto_ack=True)

    def on_response(self, ch, method, properties, body):
        if self.corr_id == properties.correlation_id:
            self.response = json.loads(body)

    def call(self, request):
        self.response = None
        self.corr_id = str(uuid.uuid4())
        self.channel.basic_publish(exchange='',
                                   routing_key='SRV.Q',
                                   properties=pika.BasicProperties(
                                         reply_to=self.callback_queue,
                                         correlation_id=self.corr_id,
                                   ),
                                   body=json.dumps(request))
        while self.response is None:
            self.connection.process_data_events()
        return self.response

def main():
    client = RpcClient()
    print(client.call({"command": "add_department", "name": "IT", "location": "Kyiv"}))
    print(client.call({"command": "search_by_department", "department_name": "IT"}))

if __name__ == "__main__":
    main()
