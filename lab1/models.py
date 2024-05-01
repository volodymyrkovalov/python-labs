import uuid

class Department:
    def __init__(self, department_id, name):
        self.department_id = department_id
        self.name = name
        self.employees = []

    def add_employee(self, name, position):
        employee_id = str(uuid.uuid4())
        new_employee = Employee(employee_id, name, position)
        self.employees.append(new_employee)

class Employee:
    def __init__(self, employee_id, name, position):
        self.employee_id = employee_id
        self.name = name
        self.position = position