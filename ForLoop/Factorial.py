# Prompt the user to enter a number and convert the input to an integer
n = int(input('Enter a Number: '))

# Initialize a variable 'fact' to store the factorial, starting with 1
fact = 1

# Loop from 1 to n (inclusive) to calculate the factorial
# The range(1, n+1) generates a sequence from 1 to n
for count in range(1, n+1):
    # Multiply the current value of 'fact' by the loop counter 'count'
    fact = fact * count

# Print the calculated factorial of the number 'n'
# The output will display the factorial with the message 'Factorial of n is'
print('Factorial of', n, 'is', fact)
