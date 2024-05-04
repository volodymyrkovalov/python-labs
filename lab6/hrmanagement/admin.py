from django.contrib import admin
from .models import Department, Employee

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'location')  # Columns to display in the admin list view
    search_fields = ('name', 'location')  # Fields to search within the admin list view

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'salary', 'department')
    list_filter = ('department', 'position')  # Filters to apply on the side of the admin list view
    search_fields = ('name', 'position', 'department__name')  # Enable search by department name

# Register your models here.
admin.site.register(Department, DepartmentAdmin)
admin.site.register(Employee, EmployeeAdmin)
