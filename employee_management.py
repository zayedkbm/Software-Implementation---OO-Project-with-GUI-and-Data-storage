import pickle
import os

EMPLOYEE_FILE_PATH = "employees.bin"


class Employee:
    def __init__(
        self,
        name,
        employee_id,
        department,
        job_title,
        basic_salary,
        age,
        date_of_birth,
        passport_details,
        manager_id=None,
    ):
        self.name = name
        self.employee_id = employee_id
        self.department = department
        self.job_title = job_title
        self.basic_salary = basic_salary
        self.age = age
        self.date_of_birth = date_of_birth
        self.passport_details = passport_details
        self.manager_id = manager_id


class EmployeeManagement:
    def __init__(self):
        self.employees = self.load_employees()

    def load_employees(self):
        if os.path.exists(EMPLOYEE_FILE_PATH):
            with open(EMPLOYEE_FILE_PATH, "rb") as file:
                return pickle.load(file)
        return {}

    def save_employees(self):
        with open(EMPLOYEE_FILE_PATH, "wb") as file:
            pickle.dump(self.employees, file)

    def add_employee(self, employee):
        if employee.employee_id in self.employees:
            raise Exception("Employee ID already exists.")
        self.employees[employee.employee_id] = employee
        self.save_employees()

    def delete_employee(self, employee_id):
        if employee_id not in self.employees:
            raise Exception("Employee not found.")
        del self.employees[employee_id]
        self.save_employees()

    def modify_employee(
        self,
        employee_id,
        name=None,
        department=None,
        job_title=None,
        basic_salary=None,
        age=None,
        date_of_birth=None,
        passport_details=None,
        manager_id=None,
    ):
        if employee_id not in self.employees:
            raise Exception("Employee not found.")
        employee = self.employees[employee_id]
        if name is not None:
            employee.name = name
        if department is not None:
            employee.department = department
        if job_title is not None:
            employee.job_title = job_title
        if basic_salary is not None:
            employee.basic_salary = basic_salary
        if age is not None:
            employee.age = age
        if date_of_birth is not None:
            employee.date_of_birth = date_of_birth
        if passport_details is not None:
            employee.passport_details = passport_details
        if manager_id is not None:
            employee.manager_id = manager_id
        self.save_employees()

    def get_employee(self, employee_id):
        if employee_id not in self.employees:
            raise Exception("Employee not found.")
        return self.employees[employee_id]

    def display_employee(self, employee_id):
        employee = self.get_employee(employee_id)
        print(f"Name: {employee.name}")
        print(f"ID Number: {employee.employee_id}")
        print(f"Department: {employee.department}")
        print(f"Job Title: {employee.job_title}")
        print(f"Basic Salary: {employee.basic_salary}")
        print(f"Age: {employee.age}")
        print(f"Date of Birth: {employee.date_of_birth}")
        print(f"Passport Details: {employee.passport_details}")
        if employee.manager_id:
            print(f"Manager ID: {employee.manager_id}")
