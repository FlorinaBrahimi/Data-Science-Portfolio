# Prompt the user to enter marks for Maths and convert the input to an integer
math = int(input('Enter Maths Marks'))

# Prompt the user to enter marks for Physics and convert the input to an integer
phy = int(input('Enter Physics Marks'))

# Prompt the user to enter marks for Chemistry and convert the input to an integer
chem = int(input('Enter Chemistry Marks'))

# Check if the marks for all three subjects are 45 or above
if math >= 45 and phy >= 45 and chem >= 45:
    # If the condition is true, print 'Passed'
    print('Passed')
# If any of the marks are below 45, print 'Failed'
else:
    print('Failed')
