# server.py
import Pyro4
import mysql.connector

@Pyro4.expose
class DepartmentManager(object):
    def __init__(self):
        self.conn = mysql.connector.connect(
            host='localhost',
            database='HRDepartment',
            user='root',
            password='password'
        )

    def add_department(self, name, location):
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO Departments (name, location) VALUES (%s, %s)", (name, location))
        self.conn.commit()
        return f"Department '{name}' added successfully."

    def get_department(self, department_id):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM Departments WHERE department_id = %s", (department_id,))
        result = cursor.fetchone()
        return result

def main():
    Pyro4.Daemon.serveSimple(
            {
                DepartmentManager: "example.departmentmanager"
            },
            ns = True)

if __name__ == "__main__":
    main()