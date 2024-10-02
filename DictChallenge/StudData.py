# Initialize an empty dictionary to store student information
Students = {}

# Loop 3 times to allow the user to input details for 3 students
for i in range(3):
    # Prompt the user to enter the student's name
    name = input('Enter name')
    
    # Prompt the user to enter the student's roll number and convert it to an integer
    roll = int(input('Enter Roll'))
    
    # Prompt the user to enter the student's department
    dept = input('Enter Dept')

    # Add a dictionary entry for the student with their name as the key
    # Store the roll number, name, and department in a nested dictionary
    Students[name] = {'Roll': roll, 'Name': name, 'Dept': dept}

# Print the dictionary containing all students' information
print(Students)
