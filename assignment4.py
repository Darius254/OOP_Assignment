class Employee:
    def __init__(self, name, employee_id, base_salary):
        self.name = name
        self.employee_id = employee_id
        self.base_salary = base_salary

    def __str__(self):
        return f"Employee ID: {self.employee_id}, Name: {self.name}"

    def calculate_salary(self):
        return self.base_salary


class FullTimeEmployee(Employee):
    def __init__(self, name, employee_id, base_salary, benefits):
        super().__init__(name, employee_id, base_salary)
        self.benefits = benefits

    def __str__(self):
        return f"Full-Time {super().__str__()}, Benefits: {self.benefits}"

    def calculate_salary(self):
        return self.base_salary + self.benefits


class PartTimeEmployee(Employee):
    def __init__(self, name, employee_id, hourly_rate, hours_worked):
        super().__init__(name, employee_id, 0)  # Part-time employees have no base salary
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def __str__(self):
        return f"Part-Time {super().__str__()}, Hourly Rate: ${self.hourly_rate}, Hours Worked: {self.hours_worked}"

    def calculate_salary(self):
        return self.hourly_rate * self.hours_worked


class Company:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def display_employees(self):
        for emp in self.employees:
            print(emp)

    def calculate_total_salary(self):
        total_salary = sum(emp.calculate_salary() for emp in self.employees)
        return total_salary


# Example Usage
company = Company()
emp1 = FullTimeEmployee("Alice", "E001", 50000, 10000)
emp2 = PartTimeEmployee("Bob", "E002", 20, 100)
company.add_employee(emp1)
company.add_employee(emp2)

company.display_employees()
total_salary = company.calculate_total_salary()
print(f"Total Salary Expense: ${total_salary}")
