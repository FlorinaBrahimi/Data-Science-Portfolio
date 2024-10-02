# Prompt the user to enter their age and convert the input to an integer
age = int(input('Enter Age'))

# Check if the age is between 18 and 60 (inclusive)
if age >= 18 and age <= 60:
    # If the age is within the range, print 'Eligible'
    print('Eligible')
# If the age is outside the range, print 'Not Eligible'
else:
    # Print 'Not Eligible' for ages below 18 or above 60
    print('Not Eligible')
