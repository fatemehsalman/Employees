class Employee:
    def __init__(self, emp_id, emp_name, emp_salary, emp_department):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.emp_salary = emp_salary
        self.emp_department = emp_department

    def calculate_emp_salary(self, hours_worked):
        if hours_worked < 0:
            raise ValueError("Hours worked cannot be negative.")
        elif hours_worked == 0:
            raise ValueError("Hours worked cannot be zero.")
        elif hours_worked > 150:
            overtime = hours_worked - 150
            overtime_amount = overtime * (self.emp_salary / 150)
            total_salary = self.emp_salary + overtime_amount
        else:
            total_salary = self.emp_salary
        return total_salary

    def emp_assign_department(self, new_department):
        self.emp_department = new_department

    def print_employee_details(self):
        print(f"Employee ID: {self.emp_id}")
        print(f"Employee Name: {self.emp_name}")
        print(f"Employee Salary: {self.emp_salary}")
        print(f"Employee Department: {self.emp_department}")
