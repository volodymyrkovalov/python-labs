from company import Company

def main():
    company = Company('employees.xml')
    company.load_data()

    # Демонстрація роботи системи
    new_dept = company.add_department('Research and Development')
    new_dept.add_employee('Alice Johnson', 'Data Scientist')
    company.save_data()

if __name__ == "__main__":
    main()