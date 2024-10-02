# Prompt the user to enter gender ('m' or 'M' for male, anything else is considered female)
gender = input('Enter Gender')

# Check if the entered gender is 'm' or 'M' (case insensitive for male)
if gender == 'm' or gender == 'M':
    # If the input is 'm' or 'M', print 'Male'
    print('Male')
# If the input is not 'm' or 'M', it is considered 'Female'
else:
    print('Female')
