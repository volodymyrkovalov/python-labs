from xml.dom.minidom import Document, parse
from models import Department, Employee


class Company:
    def __init__(self, xml_filename):
        self.xml_filename = xml_filename
        self.departments = []
        self.dom = None

    def load_data(self):
        self.dom = parse(self.xml_filename)
        company = self.dom.documentElement
        for dept_element in company.getElementsByTagName('department'):
            department_id = dept_element.getAttribute('id')
            department = Department(department_id, dept_element.getElementsByTagName('name')[0].textContent)
            self.departments.append(department)
            for emp_element in dept_element.getElementsByTagName('employee'):
                employee_id = emp_element.getAttribute('id')
                name = emp_element.getElementsByTagName('name')[0].textContent
                position = emp_element.getElementsByTagName('position')[0].textContent
                department.add_employee(name, position)

    def save_data(self):
        if self.dom is None:
            self.dom = Document()
            company = self.dom.createElement('company')
            self.dom.appendChild(company)
        else:
            company = self.dom.documentElement

        for department in self.departments:
            dept_element = self.dom.createElement('department')
            dept_element.setAttribute('id', department.department_id)
            name_element = self.dom.createElement('name')
            name_element.appendChild(self.dom.createTextNode(department.name))
            dept_element.appendChild(name_element)

            for employee in department.employees:
                emp_element = self.dom.createElement('employee')
                emp_element.setAttribute('id', employee.employee_id)
                name_element = self.dom.createElement('name')
                name_element.appendChild(self.dom.createTextNode(employee.name))
                emp_element.appendChild(name_element)
                pos_element = self.dom.createElement('position')
                pos_element.appendChild(self.dom.createTextNode(employee.position))
                emp_element.appendChild(pos_element)
                dept_element.appendChild(emp_element)

            company.appendChild(dept_element)

        with open(self.xml_filename, 'w') as file:
            self.dom.writexml(file, addindent='  ', newl='\n')

    def add_department(self, name):
        department_id = str(uuid.uuid4())
        new_department = Department(department_id, name)
        self.departments.append(new_department)
        return new_department