# Prompt the user to enter the marks and convert the input to an integer
marks = int(input('Enter Marks'))

# Check if the marks are within the valid range (0 to 100)
if marks >= 0 and marks <= 100:
    # If the marks are between 0 and 100, print 'Valid'
    print('Valid')
# If the marks are outside the range, print 'Invalid'
else:
    print('Invalid')
