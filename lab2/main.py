import mysql.connector
from mysql.connector import Error

def create_connection():
    try:
        connection = mysql.connector.connect(
            host='db',
            database='HRDepartment',
            user='root',
            password='password'
        )
        return connection
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
            print(f"Department '{name}' added successfully.")
        except Error as e:
            print(f"Error: {e}")
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
            print(f"Employee '{name}' added successfully.")
        except Error as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            conn.close()

def update_employee(employee_id, name=None, position=None, salary=None):
    conn = create_connection()
    if conn is not None:
        try:
            cursor = conn.cursor()
            updates = []
            params = []
            if name:
                updates.append("name = %s")
                params.append(name)
            if position:
                updates.append("position = %s")
                params.append(position)
            if salary:
                updates.append("salary = %s")
                params.append(salary)
            params.append(employee_id)
            update_query = ", ".join(updates)
            query = f"UPDATE Employees SET {update_query} WHERE employee_id = %s"
            cursor.execute(query, params)
            conn.commit()
            print(f"Employee ID {employee_id} updated successfully.")
        except Error as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            conn.close()

def delete_employee(employee_id):
    conn = create_connection()
    if conn is not None:
        try:
            cursor = conn.cursor()
            query = "DELETE FROM Employees WHERE employee_id = %s"
            cursor.execute(query, (employee_id,))
            conn.commit()
            print(f"Employee ID {employee_id} deleted successfully.")
        except Error as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            conn.close()

def search_employees_by_department(department_name):
    conn = create_connection()
    if conn is not None:
        try:
            cursor = conn.cursor()
            query = "SELECT e.name, e.position FROM Employees e JOIN Departments d ON e.department_id = d.department_id WHERE d.name = %s"
            cursor.execute(query, (department_name,))
            results = cursor.fetchall()
            for row in results:
                print(f"Name: {row[0]}, Position: {row[1]}")
        except Error as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            conn.close()

# Тестування функцій
if __name__ == "__main__":
    add_department('IT', 'Kyiv')
    add_employee('John Doe', 'Software Engineer', 75000, 1)
    update_employee(1, name="John Doe Jr.")
    search_employees_by_department('IT')
    delete_employee(1)