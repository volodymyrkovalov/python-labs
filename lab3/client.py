# client.py
import socket
import json

def send_request(data):
    host = 'localhost'
    port = 65432
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        s.sendall(json.dumps(data).encode())
        response = s.recv(1024)
        print('Received', response.decode())

def main():
    send_request({"command": "add_department", "name": "IT", "location": "Kyiv"})
    send_request({"command": "get_department", "department_id": 1})

if __name__ == "__main__":
    main()