# db/database.py
import mysql.connector
from mysql.connector import Error

def create_connection():
    """Створює підключення до бази даних."""
    try:
        conn = mysql.connector.connect(
            host='localhost',
            database='HRDepartment',
            user='root',
            password='password'
        )
        if conn.is_connected():
            return conn
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
        return None

def add_department(name, location):
    conn = create_connection()
    if conn is not None:
        try:
            cursor = conn.cursor()
            query = "INSERT INTO Departments (name, location) VALUES (%s, %s)"
            cursor.execute(query, (name, location))
            conn.commit()
            return {"status": "success", "message": f"Department '{name}' added successfully."}
        finally:
            cursor.close()
            conn.close()

def add_employee(name, position, salary, department_id):
    conn = create_connection()
    if conn is not None:
        try:
            cursor = conn.cursor()
            query = "INSERT INTO Employees (name, position, salary, department_id) VALUES (%s, %s, %s, %s)"
            cursor.execute(query, (name, position, salary, department_id))
            conn.commit()
            return {"status": "success", "message": f"Employee '{name}' added successfully."}
        finally:
            cursor.close()
            conn.close()

def search_employees_by_department(department_name):
    conn = create_connection()
    if conn is not None:
        try:
            cursor = conn.cursor(dictionary=True)
            query = "SELECT e.name, e.position FROM Employees e JOIN Departments d ON e.department_id = d.department_id WHERE d.name = %s"
            cursor.execute(query, (department_name,))
            results = cursor.fetchall()
            return {"status": "success", "data": results}
        finally:
            cursor.close()
            conn.close()
