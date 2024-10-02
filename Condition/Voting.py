# Prompt the user to enter their age and convert the input to an integer
age = int(input('Enter your age'))

# Check if the age is 18 or above
if age >= 18:
    # If the age is 18 or more, print 'Eligible'
    print('Eligible')
# If the age is less than 18, print 'Not Eligible'
else:
    # Print 'Not Eligible' for those under 18
    print('Not Eligible')
