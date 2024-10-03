class Department:
    def __init__(self, description):
        self.description = description
        self.manager = None
        self.employee_list = []

    def add_employee(self, employee):
        self.employee_list.append(employee)
        employee.department = self.description

    def delete_employee(self, employee):
        if employee in self.employee_list:
            self.employee_list.remove(employee)
            employee.department = None

    def set_manager(self, employee):
        if isinstance(employee, PermEmployee) and employee in self.employee_list:
            self.manager = employee

    def print_info(self):
        print(f"Department: {self.description}")
        if self.manager:
            print(f"Manager: {self.manager.name}")
        else:
            print("No manager assigned.")
        print("Employees:")
        for employee in self.employee_list:
            employee.print_info()

class Person:
    def __init__(self, name, birthdate, address):
        self.name = name
        self.birthdate = birthdate
        self.address = address

    def print_info(self):
        print(f"Name: {self.name}, Birthdate: {self.birthdate}, Address: {self.address}")


class Employee(Person):
    def __init__(self, name, birthdate, address, start_date, department=None):
        super().__init__(name, birthdate, address)
        self.start_date = start_date
        self.department = department

    def print_info(self):
        super().print_info()
        print(f"Start Date: {self.start_date}, Department: {self.department}")


class TempEmployee(Employee):
    def __init__(self, name, birthdate, address, start_date, wage):
        super().__init__(name, birthdate, address, start_date)
        self.wage = wage

    def print_info(self):
        super().print_info()
        print(f"Wage: {self.wage}")


class PermEmployee(Employee):
    def __init__(self, name, birthdate, address, start_date, salary):
        super().__init__(name, birthdate, address, start_date)
        self.salary = salary

    def print_info(self):
        super().print_info()
        print(f"Salary: {self.salary}")

dept = Department("SIIE")

emp1 = PermEmployee("Doe", "1990-01-01", "123 Main St", "2020-01-01", 50000)
emp2 = TempEmployee("Smith", "1992-05-15", "456 Elm St", "2021-05-10", 25)

dept.add_employee(emp1)
dept.add_employee(emp2)

dept.set_manager(emp1)

dept.print_info()