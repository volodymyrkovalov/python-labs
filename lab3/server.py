# server.py
import socket
import json
import mysql.connector
from mysql.connector import Error

def create_connection():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='HRDepartment',
            user='root',
            password='password'
        )
        return connection
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
        return None

def process_request(data):
    conn = create_connection()
    response = {"status": "error", "message": "Unknown command"}
    if conn is not None:
        try:
            cursor = conn.cursor(dictionary=True)
            if data['command'] == 'add_department':
                cursor.execute("INSERT INTO Departments (name, location) VALUES (%s, %s)", (data['name'], data['location']))
                conn.commit()
                response = {"status": "success", "message": "Department added successfully"}
            elif data['command'] == 'get_department':
                cursor.execute("SELECT * FROM Departments WHERE department_id = %s", (data['department_id'],))
                result = cursor.fetchone()
                response = {"status": "success", "data": result}
            cursor.close()
        except Error as e:
            response = {"status": "error", "message": str(e)}
        finally:
            conn.close()
    return response

def start_server():
    host = 'localhost'
    port = 65432
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()
        print(f"Server started at {host}:{port}")
        while True:
            conn, addr = s.accept()
            with conn:
                print('Connected by', addr)
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break
                    data = json.loads(data.decode())
                    response = process_request(data)
                    conn.sendall(json.dumps(response).encode())

if __name__ == "__main__":
    start_server()