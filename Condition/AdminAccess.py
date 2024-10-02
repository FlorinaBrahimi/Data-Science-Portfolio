# Prompt the user to enter a username
username = input('Enter Username: ')

# Check if the entered username is either 'john' or 'smith'
if username == 'john' or username == 'smith':
    print('Authorised')  # Print authorized message if the username matches
else:
    print('Not Authorised')  # Print not authorized message for any other username
