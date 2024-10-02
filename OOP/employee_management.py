class Employee:
    employee_count = 101  # Class variable to keep track of the total number of employees

    def __init__(self, name, desig, sal):
        """
        Initializes the Employee instance with a specified name, designation, and salary.

        :param name: The name of the employee
        :param desig: The designation of the employee
        :param sal: The salary of the employee
        """
        self.name = name  # Set the name attribute for the Employee object
        self.designation = desig  # Set the designation attribute for the Employee object
        self.salary = sal  # Set the salary attribute for the Employee object
        self.eid = 'e' + str(Employee.employee_count)  # Generate a unique employee ID
        Employee.employee_count += 1  # Increment the employee count for the next employee

    def show_details(self):
        """Displays the details of the employee."""
        print('Name:', self.name)  # Print the employee's name
        print('Eid:', self.eid)  # Print the employee ID
        print('Designation:', self.designation)  # Print the employee's designation
        print('Salary:', self.salary)  # Print the employee's salary

    @classmethod
    def total_emp(cls):
        """Returns the total number of employees created."""
        return cls.employee_count - 101  # Subtract the initial count to get the total


# Create instances of the Employee class with specific details
e1 = Employee('John', 'Manager', 10000)
e2 = Employee('Mark', 'Team Leader', 8000)

# Show details of the first employee
e1.show_details()
print('')  # Print a blank line for better readability

# Show details of the second employee
e2.show_details()
print('Total Employees:', e1.total_emp())  # Print the total number of employees
