# Prompt the user to enter the first number and convert the input to an integer
no1 = int(input('Enter first number'))

# Prompt the user to enter the second number and convert the input to an integer
no2 = int(input('Enter second number'))

# Check if the difference between no1 and no2 is greater than or equal to 0
if no1 - no2 >= 0:
    # If true, print the result of no1 minus no2
    print(no1 - no2)
else:
    # If false (i.e., no2 is greater), print the result of no2 minus no1
    print(no2 - no1)
