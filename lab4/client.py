# client.py
import Pyro4

def main():
    uri = "PYRONAME:example.departmentmanager"
    department_manager = Pyro4.Proxy(uri)

    # Виклик методів сервера
    print(department_manager.add_department("IT", "Kyiv"))
    print(department_manager.get_department(1))

if __name__ == "__main__":
    main()