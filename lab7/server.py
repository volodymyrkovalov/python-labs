from spyne import ComplexModel, Unicode, Integer

class Department(ComplexModel):
    __namespace__ = 'soap_service.models'
    department_id = Integer
    name = Unicode

class Employee(ComplexModel):
    __namespace__ = 'soap_service.models'
    employee_id = Integer
    first_name = Unicode
    last_name = Unicode
    department_id = Integer
