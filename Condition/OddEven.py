# Prompt the user to enter a number and convert the input to an integer
n = int(input('Enter a Number'))

# Check if the number is divisible by 2 (i.e., it's even)
if n % 2 == 0:
    # If divisible by 2, print 'Even'
    print('Even')
# If the number is not divisible by 2, it is odd
else:
    # Print 'Odd'
    print('Odd')
