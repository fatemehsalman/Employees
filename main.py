from src.emploees import Employee
"""This is the main menu"""


def main():
    employees = []

    while True:
        print("\n1. Add Employee")
        print("2. Assign Department")
        print("3. Calculate Salary")
        print("4. Print Employee Details")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            emp_id = input("Enter employee ID: ")
            emp_name = input("Enter employee name: ")
            emp_salary = float(input("Enter employee salary: "))
            emp_department = input("Enter employee department: ")
            employee = Employee(emp_id, emp_name, emp_salary, emp_department)
            employees.append(employee)
            print("Employee added successfully.")
        elif choice == "2":
            emp_id = input("Enter employee ID: ")
            for employee in employees:
                if employee.emp_id == emp_id:
                    new_department = input("Enter new department: ")
                    employee.emp_assign_department(new_department)
                    print("Department assigned successfully.")
                    break
            else:
                print("Employee not found.")
        elif choice == "3":
            emp_id = input("Enter employee ID: ")
            for employee in employees:
                if employee.emp_id == emp_id:
                    try:
                        hours_worked = float(input("Enter total hours worked: "))
                        total_salary = employee.calculate_emp_salary(hours_worked)
                        print(f"Total salary: {total_salary}")
                    except ValueError as e:
                        print(f"Error: {e}")
                    break
            else:
                print("Employee not found.")
        elif choice == "4":
            emp_id = input("Enter employee ID: ")
            for employee in employees:
                if employee.emp_id == emp_id:
                    employee.print_employee_details()
                    break
            else:
                print("Employee not found.")
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
