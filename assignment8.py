# Employee Payroll Management System

class Employee:
    def __init__(self, employee_name, employee_id, basic_salary):
        self.employee_name = employee_name
        self.employee_id = employee_id
        self.basic_salary = basic_salary

    def calculate_grade(self):
        if self.basic_salary >= 80000:
            return "A"
        elif self.basic_salary >= 60000:
            return "B"
        elif self.basic_salary >= 40000:
            return "C"
        else:
            return "D"

    def display(self):
        print("Employee Name :", self.employee_name)
        print("Employee ID   :", self.employee_id)
        print("Basic Salary  : ₹", self.basic_salary)
        print("Grade         :", self.calculate_grade())

    def __str__(self):
        return (f"Employee(Name={self.employee_name}, "
                f"ID={self.employee_id}, "
                f"Salary=₹{self.basic_salary}, "
                f"Grade={self.calculate_grade()})")


class Company:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def display_employees(self):
        if not self.employees:
            print("No employee records available.")
        else:
            print("\n--- Employee Records ---")
            for employee in self.employees:
                employee.display()
                print()


# Main Program
company = Company()

n = int(input("Enter number of employees: "))

for i in range(n):
    print(f"\nEnter details of Employee {i + 1}")
    name = input("Enter employee name: ")
    emp_id = input("Enter employee ID: ")
    salary = float(input("Enter basic salary: "))

    employee = Employee(name, emp_id, salary)
    company.add_employee(employee)

company.display_employees()


# Fibonacci using Memoization (Top-Down Dynamic Programming)

memo = {}

def fibonacci(n):
    if n in memo:
        return memo[n]

    if n <= 1:
        return n

    memo[n] = fibonacci(n - 1) + fibonacci(n - 2)
    return memo[n]


N = int(input("Enter number of Fibonacci terms: "))

print("First", N, "Fibonacci numbers:")
for i in range(N):
    print(fibonacci(i), end=" ")