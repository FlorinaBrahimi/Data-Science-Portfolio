# Prompt the user to enter the work hours for the entire week, separated by spaces
# Use list comprehension to convert the input into a list of integers
work_hours = [int(x) for x in input('Enter hours per day in entire week, separated by space: ').split()]

# Prompt the user to enter the hourly wage and convert it to an integer
wage = int(input('Enter hourly wage: '))

# Calculate the total hours worked in the week by summing the values in the work_hours list
total = sum(work_hours)

# Calculate the salary by multiplying the total hours worked by the hourly wage
salary = total * wage

# Print the calculated salary
print('Salary is', salary)
