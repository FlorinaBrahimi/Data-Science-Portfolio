# Prompt the user to enter a number and convert the input to an integer
n = int(input('Enter a Number: '))

# Loop through the numbers from 1 to n (inclusive) to find the divisors
for i in range(1, n+1):
    # Check if the current number 'i' is a divisor of 'n' by checking if the remainder is 0
    if n % i == 0:
        # If 'i' is a divisor, print it
        print(i)
