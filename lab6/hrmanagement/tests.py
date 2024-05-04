from django.test import TestCase
from django.urls import reverse
from .models import Department, Employee

class DepartmentModelTests(TestCase):
    def setUp(self):
        Department.objects.create(name="HR", location="Headquarters")

    def test_department_creation(self):
        """Tests that the department is created successfully."""
        hr = Department.objects.get(name="HR")
        self.assertEqual(hr.name, "HR")
        self.assertEqual(hr.location, "Headquarters")

class EmployeeModelTests(TestCase):
    def setUp(self):
        self.department = Department.objects.create(name="IT", location="Main Office")
        Employee.objects.create(name="John Doe", position="Developer", salary=60000, department=self.department)

    def test_employee_creation(self):
        """Tests that the employee is created with the correct attributes."""
        john = Employee.objects.get(name="John Doe")
        self.assertEqual(john.position, "Developer")
        self.assertEqual(john.salary, 60000)
        self.assertEqual(john.department.name, "IT")

class ViewsTests(TestCase):
    def setUp(self):
        self.department = Department.objects.create(name="Finance", location="Secondary Office")
        self.employee = Employee.objects.create(name="Alice Johnson", position="Accountant", salary=50000, department=self.department)

    def test_department_list_view(self):
        """Tests that the department list page loads correctly and contains department data."""
        response = self.client.get(reverse('department-list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Finance")
        self.assertContains(response, "Secondary Office")
        self.assertQuerysetEqual(
            response.context['departments'],
            ['<Department: Finance>'],
            ordered=False
        )
