# Dictionary containing names as keys and their corresponding birthdays as values
birthdays = {
    'Sachin': '03/14/2003',
    'Carl': '01/17/2001',
    'Khan': '12/10/2006',
    'Donald': '06/14/2010',
    'Rohan': '01/6/2005'
}

# Prompt the user to enter a name
name = input('Enter Name')

# Check if the entered name exists in the 'birthdays' dictionary
if name in birthdays:
    # If the name is found, print the corresponding birthday
    print('Mr./Miss {} was born on {}'.format(name, birthdays[name]))
# If the name is not found in the dictionary
else:
    # Print a message indicating that the name was not found
    print('Name is not found')
