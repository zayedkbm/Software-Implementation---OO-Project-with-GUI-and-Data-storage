import tkinter as tk
from tkinter import messagebox, ttk
from employee_management import EmployeeManagement, Employee


class EmployeeGUI:
    def __init__(self, master):
        self.master = master
        self.employee_management = EmployeeManagement()
        self.create_widgets()

    def create_widgets(self):
        # Employee ID
        tk.Label(self.master, text="Employee ID:").grid(row=0, column=0, sticky="w")
        self.employee_id_entry = tk.Entry(self.master)
        self.employee_id_entry.grid(row=0, column=1, sticky="we")

        # Name
        tk.Label(self.master, text="Name:").grid(row=1, column=0, sticky="w")
        self.name_entry = tk.Entry(self.master)
        self.name_entry.grid(row=1, column=1, sticky="we")

        # Department
        tk.Label(self.master, text="Department:").grid(row=2, column=0, sticky="w")
        self.department_entry = tk.Entry(self.master)
        self.department_entry.grid(row=2, column=1, sticky="we")

        # Job Title
        tk.Label(self.master, text="Job Title:").grid(row=3, column=0, sticky="w")
        self.job_title_entry = tk.Entry(self.master)
        self.job_title_entry.grid(row=3, column=1, sticky="we")

        # Basic Salary
        tk.Label(self.master, text="Basic Salary:").grid(row=4, column=0, sticky="w")
        self.basic_salary_entry = tk.Entry(self.master)
        self.basic_salary_entry.grid(row=4, column=1, sticky="we")

        tk.Label(self.master, text="Age:").grid(row=5, column=0, sticky="w")
        self.age_entry = tk.Entry(self.master)
        self.age_entry.grid(row=5, column=1, sticky="we")

        # Date of Birth
        tk.Label(self.master, text="Date of Birth:").grid(row=6, column=0, sticky="w")
        self.dob_entry = tk.Entry(self.master)
        self.dob_entry.grid(row=6, column=1, sticky="we")

        # Passport Details
        tk.Label(self.master, text="Passport Details:").grid(
            row=7, column=0, sticky="w"
        )
        self.passport_entry = tk.Entry(self.master)
        self.passport_entry.grid(row=7, column=1, sticky="we")

        # Manager ID
        tk.Label(self.master, text="Manager ID:").grid(row=8, column=0, sticky="w")
        self.manager_id_entry = tk.Entry(self.master)
        self.manager_id_entry.grid(row=8, column=1, sticky="we")

        # Buttons for operations
        self.add_button = tk.Button(
            self.master, text="Add Employee", command=self.add_employee
        )
        self.add_button.grid(row=9, column=0, sticky="we")

        self.delete_button = tk.Button(
            self.master, text="Delete Employee", command=self.delete_employee
        )
        self.delete_button.grid(row=9, column=1, sticky="we")

        self.modify_button = tk.Button(
            self.master, text="Modify Employee", command=self.modify_employee
        )
        self.modify_button.grid(row=10, column=0, sticky="we")

        self.display_button = tk.Button(
            self.master, text="Display Employee", command=self.display_employee
        )
        self.display_button.grid(row=10, column=1, sticky="we")

    def add_employee(self):
        try:
            new_employee = Employee(
                name=self.name_entry.get(),
                employee_id=self.employee_id_entry.get(),
                department=self.department_entry.get(),
                job_title=self.job_title_entry.get(),
                basic_salary=self.basic_salary_entry.get(),
                age=self.age_entry.get(),
                date_of_birth=self.dob_entry.get(),
                passport_details=self.passport_entry.get(),
                manager_id=self.manager_id_entry.get() or None,
            )
            self.employee_management.add_employee(new_employee)
            messagebox.showinfo("Success", "Employee added successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"Could not add employee: {e}")

    def delete_employee(self):
        employee_id = self.employee_id_entry.get()
        try:
            self.employee_management.delete_employee(employee_id)
            messagebox.showinfo("Success", "Employee deleted successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"Could not delete employee: {e}")

    def modify_employee(self):
        employee_id = self.employee_id_entry.get()
        try:
            self.employee_management.modify_employee(
                employee_id,
                name=self.name_entry.get(),
                department=self.department_entry.get(),
                job_title=self.job_title_entry.get(),
                basic_salary=self.basic_salary_entry.get(),
                age=self.age_entry.get(),
                date_of_birth=self.dob_entry.get(),
                passport_details=self.passport_entry.get(),
                manager_id=self.manager_id_entry.get() or None,
            )
            messagebox.showinfo("Success", "Employee modified successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"Could not modify employee: {e}")

    def display_employee(self):
        employee_id = self.employee_id_entry.get()
        try:
            employee = self.employee_management.get_employee(employee_id)
            employee_info = (
                f"Name: {employee.name}\n"
                f"Department: {employee.department}\n"
                f"Job Title: {employee.job_title}\n"
                f"Basic Salary: {employee.basic_salary}\n"
                f"Age: {employee.age}\n"
                f"Date of Birth: {employee.date_of_birth}\n"
                f"Passport Details: {employee.passport_details}\n"
                f"Manager ID: {employee.manager_id}"
            )
            messagebox.showinfo("Employee Details", employee_info)
        except Exception as e:
            messagebox.showerror("Error", f"Could not display employee: {e}")
